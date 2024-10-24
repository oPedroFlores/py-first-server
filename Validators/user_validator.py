from pydantic import BaseModel, Field, validator

class UserCreateSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)

    @validator('username')
    def name_must_be_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('must be alphanumeric')
        if len(v) < 3 or len(v) > 50:
            raise ValueError('Username precisa ter entre 3 e 50 caracteres.')
        return v

    @validator('email')
    def email_must_contain_at_symbol(cls, v):
        if '@' not in v:
            raise ValueError('must contain @ symbol')
        return v
    
    @validator('password')
    def password_must_contain_at_symbol(cls, v):
        if not v.isalnum():
            raise ValueError('must contain alphanumeric')
        return v