from sqlalchemy import Column, Integer, Text, Index, DateTime, ForeignKey
from sqlalchemy.sql import func

from .meta import Base


class Ret(Base):
    __tablename__ = 'Ret'
    id = Column(Integer, primary_key=True)
    fk_menu = Column(Integer, ForeignKey('Menu.id'))
    item = Column(Text, nullable=False)
    sortering = Column(Integer, nullable=False)
    oprettet = Column(DateTime(timezone=True), server_default=func.now())
    oprettet_af = Column(Text)
    aendret = Column(DateTime(timezone=True), onupdate=func.now())
    aendret_af = Column(Text)


Index('ix_ret', Ret.id, unique=True, mysql_length=255)
