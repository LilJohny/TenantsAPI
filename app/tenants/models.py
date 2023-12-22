from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON

from database import Base


class TenantModel(Base):
    __tablename__ = 'tenants'

    number = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String, nullable=False, index=True)

    info = Column(JSON)
