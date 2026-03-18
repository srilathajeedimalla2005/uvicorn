import httpx

API_KEY = "YOUR_API_KEY"

async def analyze_data(sector, data):

    prompt = f"""
    Analyze {sector} sector in India:

    {data}

    Give:
    - Summary
    - Opportunities
    - Risks
    """

    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent",
            params={"key": API_KEY},
            json={
                "contents": [{"parts": [{"text": prompt}]}]
            },
        )

    return res.json()