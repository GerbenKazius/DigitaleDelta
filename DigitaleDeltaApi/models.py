from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, BigInteger, Boolean, ForeignKey
Base = declarative_base()

class Reference(Base):
    __tablename__ = 'Reference'
    __table_args__ = {'schema': 'DigitaleDelta'}
    Id = Column(String(100), primary_key=True)
    Type = Column(String)
    Organisation = Column(String)
    Code = Column(String)
    Geography = Column(String)
    Description = Column(String)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Result(Base):
    __tablename__ = 'Result'
    __table_args__ = {'schema': 'DigitaleDelta'}
    Id = Column(String(100), primary_key=True)
    Truth = Column(Boolean)
    Count = Column(BigInteger)
    Geography = Column(String)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Observation(Base):
    __tablename__ = 'Observation'
    __table_args__ = {'schema': 'DigitaleDelta'}
    Id = Column(String(100), primary_key=True)
    Type = Column(String, nullable=False)
    ResultTime = Column(DateTime, nullable=False)
    PhenomenonTime = Column(DateTime, nullable=False)
    ValidTime = Column(DateTime)
    FoiId = Column(String(100), ForeignKey('DigitaleDelta.Reference.Id'))
    ResultId = Column(String(100), ForeignKey('DigitaleDelta.Result.Id'), nullable=False)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
