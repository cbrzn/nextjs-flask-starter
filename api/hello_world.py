from .app import app

@app.get("/api/siu")
async def siu():
    return "<h1>SIUUUUUUUUUUUUUUUUUUUUU</h1>"