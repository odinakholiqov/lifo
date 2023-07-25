from pydantic import BaseModel, root_validator
from typing import Optional
from datetime import date

class CreateBlog(BaseModel):
    title: str
    slug: str
    context: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if 'title' in values:
            values['slug'] = values.get("title").replace(" ", "-").lower()
        return values

class ShowBlog(BaseModel):
    # title: str
    # context: Optional[str]

    title: str
    slug: str
    context: Optional[str] = None

    class Config():
        from_attributes = True

class UpdateBlog(CreateBlog):
    pass