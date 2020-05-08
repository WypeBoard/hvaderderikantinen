from sqlalchemy import Column, Integer, Text, Index, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .meta import Base


class Menu(Base):
    __tablename__ = 'Menu'
    id = Column(Integer, primary_key=True)
    fk_ret = relationship('Ret')
    dato = Column(Date)
    oprettet = Column(Text)
    oprettet_af = Column(DateTime(timezone=True), server_default=func.now())
    aendret = Column(Text)
    aendret_af = Column(DateTime(timezone=True), onupdate=func.now())


Index('ix_menu', Menu.id, unique=True, mysql_length=255)
