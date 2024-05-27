from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base, created_at, uuidpk


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[uuidpk]
    tg_id: Mapped[int] = mapped_column(unique=True, index=True)
    # username: Mapped[str]
    created_at: Mapped[created_at]


Tables = [UserModel]
