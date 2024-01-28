from fastapi import APIRouter, HTTPException, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app.database import get_db
from app.tenants.models import TenantModel
from app.tenants.schemas import TenantInSchema, TenantOutSchema

tenants_router = APIRouter(prefix="/tenants",
                           tags=["tenants"], )


@tenants_router.get("/{tenant_id}")
def get_tenant(tenant_id: str, db: Session = Depends(get_db)) -> TenantOutSchema:
    tenant = db.query(TenantModel).filter(TenantModel.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant


@tenants_router.get("/")
def list_tenants(db: Session = Depends(get_db)) -> Page[TenantOutSchema]:
    tenants_query = db.query(TenantModel).order_by(TenantModel.number)
    return paginate(tenants_query)


@tenants_router.post("/")
def create_tenant(tenant_data: TenantInSchema, db: Session = Depends(get_db)) -> TenantOutSchema:
    tenant = TenantModel(**tenant_data.dict())

    db.add(tenant)
    db.flush()

    tenant.id = ''.join([str(tenant.number), tenant.id])
    db.commit()

    return TenantOutSchema.model_validate(tenant)
