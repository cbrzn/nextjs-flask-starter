from .app import app

@app.get("/api/yo")
async def yo():
    return "hello from /api/yo"