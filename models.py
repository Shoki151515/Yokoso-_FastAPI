from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from settings import Base


class TodoModel(Base):
    __tablename__ = 'Event'

    festival_id = Column(Integer, primary_key=True)
    festival_description = Column(String)
    festival_img =Column(String)
    festival_data = Column(DateTime)
    festival_address = Column(String)
    festival_start_time = (DateTime)
    festival_end_time = Column(DateTime)
    created_date = Column(DateTime, default=datetime.utcnow)


