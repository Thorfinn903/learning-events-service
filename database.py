from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost/learning_events"
SQLALCHEMY_DATABASE_URL = "sqlite:///./learning_events_v2.db"

# connecting to the database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# helper function to get the db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()