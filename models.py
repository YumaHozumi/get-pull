from sqlalchemy import Column, Integer, String
from database import Base

class PullReq(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    pullreq_id = Column(Integer)