from fastapi import FastAPI
from fastapi_pagination import add_pagination

from tenants import tenants_router

app = FastAPI()
add_pagination(app)

app.include_router(tenants_router)

