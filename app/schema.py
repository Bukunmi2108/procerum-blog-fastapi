from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    subheading: str
    content: str
    author: str
    tags: list

class UpdateBlog(BaseModel):
    title: str = None
    subheading: str = None
    content: str = None
    author: str = None
    tags: list = None