from .main import app

@app.get("/api/yo")
async def another_endpoint():
    return "<h1>SIUUUUUUUUUUUUUUUUUUUUU</h1>"