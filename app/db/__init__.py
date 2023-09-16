from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, sessionmaker

from app.settings import settings

# Docs: https://docs.sqlalchemy.org/en/20/core/engines.html#creating-urls-programmatically
url_object = URL.create(
    drivername=settings.DB_DRIVER_NAME,
    host=settings.DB_HOST,
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    database=settings.DB_NAME,
)
db_url = url_object.render_as_string(hide_password=False)

engine = create_engine(url_object)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Use `MappedAsDataclass` instead of `declarative_base` for autocompletion
class Base(MappedAsDataclass, DeclarativeBase):
    pass
