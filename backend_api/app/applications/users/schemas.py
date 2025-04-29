from pydantic import BaseModel, EmailStr, Field

class BaseFields(BaseModel):
    email: EmailStr = Field(description='User email', examples=['artem.chebanyuk@gmail.com'])
    name: str = Field(description='User nickname', example=['Casper'])

class PasswordField(BaseModel):
    password: str = Field(min_lenght=8)

class RegisterUserFields(BaseFields, PasswordField):
    pass
