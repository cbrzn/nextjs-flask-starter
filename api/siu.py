from .app import app

@app.get("/api/siu")
async def siu():
    return "hello from /api/siu"