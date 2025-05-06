from pydantic import BaseModel, EmailStr, Field, ValidationInfo, model_validator


class BaseFields(BaseModel):
    email: EmailStr = Field(description="User email", examples=["artem.chebanyuk@gmail.com"])
    name: str = Field(description="User nickname", example=["Casper"])


class PasswordField(BaseModel):
    password: str = Field(min_lenght=8)

    @model_validator(mode="before")
    def validate_password(cls, values: dict, info: ValidationInfo) -> dict:
        password = (values.get("password") or "").strip()
        if not password:
            raise ValueError("Password required")
        if len(password) < 8:
            raise ValueError("Password is too short")
        if " " in password:
            raise ValueError("Space in password")


class RegisterUserFields(BaseFields, PasswordField):
    pass
