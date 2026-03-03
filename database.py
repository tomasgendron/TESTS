import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Check if running on Azure, otherwise default to local
if 'WEBSITE_HOSTNAME' in os.environ:
    # Use the persistent /home directory on Azure
    # Ensure the /home/data folder exists manually in Kudu or via os.makedirs
    db_path = "/home/data/sql_app.db"
    
    # Optional: Auto-create the directory if it doesn't exist
    if not os.path.exists("/home/data"):
        os.makedirs("/home/data")
else:
    # Your original local path for VS Code
    db_path = "./sql_app.db"

SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
