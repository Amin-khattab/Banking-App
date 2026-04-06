from fastapi import FastAPI, Request, Form,Depends,Query
from pathlib import Path
from sqlalchemy.orm import Session
from sqlalchemy import func
from passlib.context import CryptContext
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse,RedirectResponse
import re
from fastapi.templating import Jinja2Templates
from Back_end.database import get_db
from Back_end.models import User , Transaction
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")

BASE_DIR = Path(__file__).resolve().parent.parent
FRONT_END_DIR = BASE_DIR / "front_end"
EMAIL_REG = r"^[^@]+@[^@]+\.[^@]+$"

template = Jinja2Templates(directory=str(FRONT_END_DIR))

app.add_middleware(SessionMiddleware,secret_key = "super-secret-key")
app.mount("/static",StaticFiles(directory=FRONT_END_DIR),name="static")

@app.get("/")
def sign_up_page(request: Request):
    return template.TemplateResponse(request,"sign_up.html")

@app.get("/login")
def login_page():
    return FileResponse(FRONT_END_DIR / "login.html")

@app.get("/dashboard")
def dashboard_page(request:Request, db : Session = Depends(get_db)):
    if "user_id" not in request.session:
        return RedirectResponse("/login",status_code=303)
    
    user_id = request.session["user_id"]
    transaction = db.query(Transaction).filter(Transaction.user_id == user_id).all()
    user = db.query(User).filter(User.id == user_id).first()

    income_total = sum(float(t.amount) for t in transaction if t.type == "income")
    expense_total = sum(float(t.amount) for t in transaction if t.type == "expense")
    balance = float(user.balance)
    recent_transactions = db.query(Transaction).filter(Transaction.user_id == user_id).order_by(Transaction.created_at.desc()).limit(5).all()

    return template.TemplateResponse(request,"dashboard.html",
                                     {"transactions":recent_transactions,
                                      "income_total":income_total,
                                      "expense_total":expense_total,
                                      "balance":balance})

@app.get("/transaction")
def transaction_page(request:Request,db: Session = Depends(get_db),type : str | None = Query(default=None)):
    if "user_id" not in request.session:
        return RedirectResponse("/login",status_code=303)
    
    user_id = request.session["user_id"]
    query = db.query(Transaction).filter(Transaction.user_id == user_id)
    
    if type == "income":
        query = query.filter(Transaction.type == "income")
    elif type == "expense":
        query = query.filter(Transaction.type == "expense")

    transactions = query.all()

    return template.TemplateResponse(request,"transaction.html",{"transactions":transactions,
                                                                 "selected_type":type})

@app.get("/transfer")
def transfer_page(request:Request):
    if "user_id" not in request.session:
        return RedirectResponse("/login",status_code=303)
    return FileResponse(FRONT_END_DIR / "transfer.html")

@app.post("/transfer")
def handle_transfer(request:Request,
                    email : str = Form(...),
                    amount : float = Form(...),
                    db : Session = Depends(get_db)):
    
    if "user_id" not in request.session:
        return RedirectResponse("/login",status_code=303)
    email = email.strip().lower()

    if not email:
        return RedirectResponse("/transfer",status_code=303)
    if amount <= 0:
        return RedirectResponse("/transfer",status_code=303)
    
    sender_id = request.session["user_id"]

    sender = db.query(User).filter(User.id == sender_id).first()
    recipient = db.query(User).filter(func.lower(User.email) == email).first()

    if not sender:
        return RedirectResponse("/login",status_code=303)
    if not recipient:
        return RedirectResponse("/transfer",status_code=303)
    if recipient.id == sender.id:
        return RedirectResponse("/transfer",status_code=303)
    if float(sender.balance) < amount:
        return RedirectResponse("/transfer",status_code=303)
    
    sender.balance = float(sender.balance) - amount
    recipient.balance = float(recipient.balance) + amount

    sender_transaction = Transaction(
        user_id = sender.id,
        title = f"Transfer to {recipient.email}",
        category = "transfer",
        amount = amount,
        type = "expense"
    )

    recipient_transaction = Transaction(
        user_id = recipient.id,
        title = f"Transfer from {sender.email}",
        category = "transfer",
        amount = amount,
        type = "income"
    )


    db.add(sender_transaction)
    db.add(recipient_transaction)
    db.commit()

    return RedirectResponse("/transaction",status_code=303)
    

@app.get("/cards")
def cards_page(request:Request):
    if "user_id" not in request.session:
        return RedirectResponse("/login",status_code=303)
    return FileResponse(FRONT_END_DIR / "cards.html")


@app.get("/profile")
def profile_page(request:Request):
    if "user_id" not in request.session:
        return RedirectResponse("/login",status_code=303)
    return FileResponse(FRONT_END_DIR / "profile.html")

@app.post("/handle_login")
def login(request : Request,
          email : str = Form(...),
          password : str = Form(...),
          db : Session = Depends(get_db)):

    email = email.strip().lower()
    existing_user = db.query(User).filter(func.lower(User.email) == email).first()

    if existing_user and pwd_context.verify(password , existing_user.hashed_password):  
        request.session["user_id"] = existing_user.id
        return {"success":True , "redirect": "/dashboard" }
    else:
        return {"success":False , "error": "This user doesnt Exist" }
    

@app.post("/sign_up")
def handle_sign_up(request:Request,
                    email: str = Form(...),
                    password: str = Form(...),
                    db : Session = Depends(get_db)):

    email = email.strip().lower()

    if not re.fullmatch(EMAIL_REG, email):
        return {"success": False, "error": "Please enter a valid email."}
    
    existing_user = db.query(User).filter(User.email == email).first()
    
    if existing_user:
        return {"success":False,"error":"this email already exists, try another one"}

    if not password or len(password) < 8:
        return {"success": False, "error": "Password must be at least 8 characters long."}
    
    hashed_password = pwd_context.hash(password)

    new_user = User(
        email=email,
        hashed_password = hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    request.session["user_id"] = new_user.id

    return {"success": True, "redirect": "/dashboard"}


@app.post("/logout")
def logout(request:Request):
    request.session.clear()
    return RedirectResponse("/login",status_code=303)
