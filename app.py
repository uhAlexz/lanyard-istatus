from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import httpx
from pathlib import Path

import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

IMAGE_DIR = "images"

@app.get("/user_status/{user_id}")
async def get_user_status(user_id: int, type: str = Query(default="normal")):
    api_url = f"https://api.lanyard.rest/v1/users/{user_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)

    if response.is_success:
        data = response.json()
        discord_status = data.get("data", {}).get("discord_status")

        if discord_status is None:
            raise HTTPException(status_code=404, detail="Discord status not found.")
        
        image_name = f"{discord_status}_status_{type}.png"
        image_path = os.path.join(IMAGE_DIR, image_name)

        if not os.path.exists(image_path):
            raise HTTPException(status_code=404, detail="Image not found.")
        
        return FileResponse(image_path, media_type="image/png")


    else:
        raise HTTPException(status_code=404, detail="User not found.")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

if __name__ == "__app__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
