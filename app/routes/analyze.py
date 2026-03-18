from fastapi import APIRouter, Depends, HTTPException
from services.data_collector import fetch_sector_news
from services.ai_service import analyze_data
from services.report_builder import build_markdown
from core.auth import verify_token
from core.rate_limiter import limiter
from fastapi import Request

router = APIRouter()

@router.get("/analyze/{sector}")
@limiter.limit("5/minute")


async def analyze_sector(request: Request, sector: str, user=Depends(verify_token)):

    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Invalid sector")

    try:
        data = await fetch_sector_news(sector)
        analysis = await analyze_data(sector, data)
        report = build_markdown(sector, analysis)

        return {"report": report}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))