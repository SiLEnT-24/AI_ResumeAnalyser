from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL=""

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl":{
            "ssl":True
        }
    }
)

SessionLocal= sessionmaker(bind=engine)
Base = declarative_base()

