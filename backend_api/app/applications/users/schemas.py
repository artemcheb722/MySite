from pydantic import BaseModel, EmailStr, Field

class UserFields(BaseModel):
    email: EmailStr = Field(description='User email', examples=['artem.chebanyuk@gmail.com'])
    name: str = Field(description='User nickname', example=['Casper'])
