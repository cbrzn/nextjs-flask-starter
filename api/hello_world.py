from fastapi import FastAPI 

app = FastAPI()

@app.get("/api/siu")
async def hello_world():
    return "<h1>SIUUUUUUUUUUUUUUUUUUUUU</h1>"