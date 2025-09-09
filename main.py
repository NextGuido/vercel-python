import time

from fastapi import FastAPI

app = FastAPI()  # 直接创建FastAPI实例


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI on Vercel!"}


@app.get("/task")
async def read_task(seconds: int):
    time.sleep(seconds)
    return {"message": "task done"}


# Vercel 会自动识别并托管这个 'app' 实例[7](@ref)
