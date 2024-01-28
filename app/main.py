import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.tenants import tenants_router

app = FastAPI()
add_pagination(app)

app.include_router(tenants_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
