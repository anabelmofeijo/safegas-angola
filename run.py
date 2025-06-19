from app import FastAPI, CORSMiddleware
from app.routers import reading_router, alert_router
from app.routers import auth_router, control_router
from app.routers import sensor_router
from app.config import Base, engine
from app.models import (
    alert_model,
    auth_model,
    control_model,
    reading_model,
    sensor_model
)


app = FastAPI(title="SafeGas API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(reading_router.router, prefix="/reading", tags=["reading"])
app.include_router(alert_router.router, prefix="/alert", tags=["alert"])
app.include_router(auth_router.router, prefix="/auth", tags=["auth"])
app.include_router(control_router.router, prefix="/control", tags=["control"])
app.include_router(sensor_router.router, prefix="/sensor", tags=["sensor"])

@app.get("/")
async def start():
    return {"message": "API is running"}