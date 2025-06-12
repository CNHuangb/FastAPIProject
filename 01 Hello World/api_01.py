import uvicorn
from fastapi import FastAPI

app = FastAPI()



@app.get("/",tags=["测试api"],
         summary="summary",
         description="description",
         response_description="response_description"
         )

def read_items():
    
    return "hello world"



# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar3"}]}
#     if q:
#         results.update({"q": q})
#     return results





if __name__ == '__main__':
    uvicorn.run("api_01:app", port=8000, reload=True)