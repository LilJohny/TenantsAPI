from pydantic import BaseModel, validator


class TenantInSchema(BaseModel):
    id: str
    info: dict


class TenantOutSchema(TenantInSchema):
    number: int

    class Config:
        from_attributes = True


class TenantSchema(TenantOutSchema):

    @validator('number')
    def id_starts_with_number(cls, val, values):
        id_ = values.get('id')
        if id_ is None:
            raise ValueError('Id is not set')
        if not id_.startswith(str(val)):
            raise ValueError(f'id must start with the number {val}')
        return val
