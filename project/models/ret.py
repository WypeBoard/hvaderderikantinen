from sqlalchemy import Column, Integer, Text, Index, DateTime, ForeignKey
from sqlalchemy.sql import func

from .meta import Base


class Ret(Base):
    __tablename__ = 'Ret'
    id = Column(Integer, primary_key=True)
    fk_menu = Column(Integer, ForeignKey('Menu.id'))
    item = Column(Text)
    ret_type = Column(Text)
    oprettet = Column(Text)
    oprettet_af = Column(DateTime(timezone=True), server_default=func.now())
    aendret = Column(Text)
    aendret_af = Column(DateTime(timezone=True), onupdate=func.now())


Index('ix_ret', Ret.id, unique=True, mysql_length=255)
