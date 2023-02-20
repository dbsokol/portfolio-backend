from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_NAME = "postgres"
DB_HOST = "portfolio.c4oxatujzf5i.us-east-1.rds.amazonaws.com"
DB_USER = "postgres"
DB_PASS = "Hellohi123!"


engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
)
connection = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
