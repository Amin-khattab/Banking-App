from sqlalchemy import DateTime, String, func,ForeignKey,Numeric,text
from sqlalchemy.orm import Mapped, mapped_column
from Back_end.database import Base

class User(Base):
    __tablename__ = "users"
    balance: Mapped[float] = mapped_column(
        Numeric(10,2),nullable=False,server_default=text("10000.00")
    )
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id") , nullable=False)
    title : Mapped[str] = mapped_column(String(length=255),nullable=False)
    category : Mapped[str] = mapped_column(String(length=255),nullable=False)
    amount : Mapped[int] = mapped_column(Numeric(10,2),nullable=False)
    type : Mapped[str] = mapped_column(String(length=100),nullable=False)
    created_at : Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),server_default=func.now(),nullable=False
    )


