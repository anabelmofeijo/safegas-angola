from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import datetime
from enum import Enum
from sqlalchemy import (
    Column, 
    Integer,
    String,
    Boolean,
    DateTime
)
from app.config import Base, db


router = APIRouter()

