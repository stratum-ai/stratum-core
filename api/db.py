from __future__ import annotations

import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Tenant(Base):
    __tablename__ = "tenants"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    slug: Mapped[str] = mapped_column(unique=True, index=True)
    name: Mapped[str]


def get_db_url() -> str:
    return os.getenv("STRATUM_DB_URL", "postgresql://stratum:stratum@localhost:5432/stratum")


def get_engine():
    return create_engine(get_db_url(), pool_pre_ping=True)


def init_db() -> None:
    engine = get_engine()
    Base.metadata.create_all(engine)


def session_scope() -> Generator[Session, None, None]:
    engine = get_engine()
    with Session(engine) as session:
        yield session


