from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class ColCreatedAt:
    # `nullable=False` prevents `null` value even if we explicitly/accidentally try to
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        init=False,
    )


class ColUpdatedAt:
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
        nullable=True,
        init=False,
    )


class InsertMeta(ColCreatedAt, ColUpdatedAt):
    pass
