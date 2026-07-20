import os
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import declarative_base, sessionmaker

# TiDB connection variables; fall back to SQLite if not configured.
tidb_user = os.getenv("TIDB_USER", os.getenv("USERNAME"))
tidb_password = os.getenv("TIDB_PASSWORD", os.getenv("PASSWORD"))
tidb_host = os.getenv("TIDB_HOST", os.getenv("HOST"))
tidb_port = int(os.getenv("TIDB_PORT", os.getenv("PORT", "4000")))
tidb_db_name = os.getenv("TIDB_DATABASE", os.getenv("DATABASE", "test"))
ca_path = os.getenv("TIDB_CA", os.getenv("CA", ""))


def get_db_engine():
    connect_args = {}
    if ca_path and ca_path != "<CA_PATH>":
        connect_args = {
            "ssl_verify_cert": True,
            "ssl_verify_identity": True,
            "ssl_ca": ca_path,
        }

    if tidb_user and tidb_password and tidb_host and tidb_db_name:
        return create_engine(
            URL.create(
                drivername="mysql+pymysql",
                username=tidb_user,
                password=tidb_password,
                host=tidb_host,
                port=tidb_port,
                database=tidb_db_name,
            ),
            pool_pre_ping=True,
            connect_args=connect_args,
        )

    return create_engine(
        "sqlite:///./resume.db",
        pool_pre_ping=True,
        connect_args={"check_same_thread": False},
    )


engine = get_db_engine()
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

