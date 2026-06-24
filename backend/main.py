from fastapi import FastAPI
from procure_track.routers import router

app = FastAPI(
    title="Procurement and Invoice Monitoring App",
    version="0.1.0"
)

app.include_router(router)

@app.get("/")
async def root():
    return {"status": "app is running"}