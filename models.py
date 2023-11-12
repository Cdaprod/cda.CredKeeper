from pydantic import BaseModel, SecretStr, Field, Column, String, Enum
from typing import Optional, Dict
import enum
from . import Base

class CredentialType(enum.Enum):
    API_KEY = "API Key"
    TOKEN = "Token"
    SSH_KEY = "SSH Key"
    DATABASE = "Database"
    OAUTH = "OAuth"
    OTHER = "Other"
    
    
class Credential(BaseModel):
    name: str
    type: CredentialType
    value: SecretStr
    details: Optional[Dict[str, str]] = Field(default_factory=dict)

    class Config:
        orm_mode = True
        
class CredentialDB(Base):
    __tablename__ = "credentials"

    name = Column(String, primary_key=True, index=True)
    type = Column(Enum(CredentialType))
    value = Column(String)
    details = Column(String)  # This can be JSON or a serialized string