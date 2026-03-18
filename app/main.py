from fastapi import FastAPI
from routes.analyze import router as analyze_router
from fastapi.responses import FileResponse
from app.routes.analyze import router as analyze_router

app = FastAPI()

app.include_router(analyze_router)





@app.get("/favicon.ico")
async def favicon():
    return FileResponse("favicon.ico")