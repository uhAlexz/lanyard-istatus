from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, RedirectResponse
import httpx
from pathlib import Path
import os

app = FastAPI()

IMAGE_DIR = Path("images")

@app.get("/user_status/{user_id}")
async def get_user_status(user_id: int):
    api_url = f"https://api.lanyard.rest/v1/users/{user_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)

    if response.is_success:
        data = response.json()
        discord_status = data.get("data", {}).get("discord_status")

        if discord_status is None:
            raise HTTPException(status_code=404, detail="Discord status not found.")
        
        image_name = f"{discord_status}_status.png"
        image_path = IMAGE_DIR / image_name

        if not image_path.exists():
            raise HTTPException(status_code=404, detail="Image not found.")
        
        return FileResponse(image_path, media_type="image/png")
    else:
        raise HTTPException(status_code=404, detail="User not found.")

@app.get("/")
async def home():
    return RedirectResponse(url="https://github.com/phineas/lanyard")

if __name__ == "__app__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
