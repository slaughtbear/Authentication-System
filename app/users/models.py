from datetime import datetime

from sqlalchemy import DateTime, Identity, Text, func, true
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    username: Mapped[str] = mapped_column(Text, unique=True)
    hashed_password: Mapped[str] = mapped_column(Text)
    is_active: Mapped[bool] = mapped_column(server_default=true())
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
