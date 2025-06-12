import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["测试api"], summary="summary", description="description", response_description="response_description")

async def root():
    return {"message": "Hello World"}



if __name__ == '__main__':
    uvicorn.run("api_02:app", port=8000, reload=True)