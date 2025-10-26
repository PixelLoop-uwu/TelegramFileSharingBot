from sqlalchemy import Column, Integer, String, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
  __tablename__ = "UserFiles"
  user_id = Column(Integer, primary_key=True)
  files = relationship("File", back_populates="user", cascade="all, delete-orphan")

class File(Base):
  __tablename__ = "files"
  file_id = Column(String, primary_key=True)
  user_id = Column(Integer, ForeignKey("UserFiles.user_id"), nullable=False)
  file_name = Column(String, nullable=False)
  size = Column(BigInteger, nullable=False)
  upload_time = Column(DateTime, nullable=False)
  downloads = Column(Integer, default=0)
  download_id = Column(String, nullable=False) 

  user = relationship("User", back_populates="files")