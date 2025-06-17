
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Caminho absoluto da raiz do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho da pasta do banco
DB_DIR = os.path.join(BASE_DIR, 'app', 'db')  
os.makedirs(DB_DIR, exist_ok=True)  # Cria a pasta se não existir

# Caminho completo do banco
DATABASE_URL = f"sqlite:///{os.path.join(DB_DIR, 'database.db')}"

# Engine com configuração especial para SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

Base = declarative_base()
