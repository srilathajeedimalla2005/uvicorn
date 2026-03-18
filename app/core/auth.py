from fastapi import Header, HTTPException

API_KEY = "secret123"

def verify_token(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True