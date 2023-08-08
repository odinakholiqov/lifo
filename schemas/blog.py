from typing import Optional

from pydantic import BaseModel
from pydantic import model_validator


class CreateBlog(BaseModel):
    title: str
    slug: str
    context: Optional[str] = None

    @model_validator(mode="before")
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values


class ShowBlog(BaseModel):
    id: int
    title: str
    slug: str
    context: Optional[str] = None

    class ConfigDict:
        from_attributes = True


class UpdateBlog(CreateBlog):
    pass


class DeleteBlog(CreateBlog):
    pass
