import httpx

async def fetch_sector_news(sector: str):
    query = f"{sector} India news"

    url = f"https://duckduckgo.com/?q={query}&format=json"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    return response.text[:1000]