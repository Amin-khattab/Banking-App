from fastapi import FastAPI, Request, Form
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import re
from fastapi.templating import Jinja2Templates

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent
FRONT_END_DIR = BASE_DIR / "front_end"
EMAIL_REG = r"^[^@]+@[^@]+\.[^@]+$"
template = Jinja2Templates(directory=str(FRONT_END_DIR))

app.mount("/static",StaticFiles(directory=FRONT_END_DIR),name="static")

@app.get("/")
def sign_up_page(request: Request):
    return template.TemplateResponse({"request": request},"sign_up.html")

@app.get("/dashboard")
def dashboard_page():
    return FileResponse(FRONT_END_DIR / "dashboard.html")

@app.get("/transaction")
def transaction_page():
    return FileResponse(FRONT_END_DIR / "transaction.html")

@app.get("/transfer")
def transfer_page():
    return FileResponse(FRONT_END_DIR / "transfer.html")

@app.get("/cards")
def cards_page():
    return FileResponse(FRONT_END_DIR / "cards.html")


@app.get("/profile")
def profile_page():
    return FileResponse(FRONT_END_DIR / "profile.html")

@app.post("/sign_up")
def handle_sign_up(email: str = Form(...), password: str = Form(...)):
    if not re.fullmatch(EMAIL_REG, email):
        return {"success": False, "error": "Please enter a valid email."}

    if not password or len(password) < 8:
        return {"success": False, "error": "Password must be at least 8 characters long."}

    return {"success": True, "redirect": "/dashboard"}

