from uuid import UUID
from pydantic import BaseModel, Field, field_validator


class ListBlogPostResponse(BaseModel):
    id: UUID
    title: str
    n_comments: int

    class Config:
        from_attributes = True


class CreateBlogPost(BaseModel):
    title: str
    content: str


class CreateBlogPostResponse(BaseModel):
    id: UUID
    title: str
    content: str

    class Config:
        from_attributes = True


class Comment(BaseModel):
    content: str

    class Config:
        from_attributes = True


class BlogPostResponse(BaseModel):
    title: str
    content: str
    comments: list[Comment] = Field(alias='comment_set')

    @field_validator('comments', mode='before')
    @classmethod
    def convert_comments(cls, value):
        return list(value.all())

    class Config:
        from_attributes = True


class CreateComment(BaseModel):
    content: str


class CreateCommentResponse(BaseModel):
    id: UUID
    content: str
    post_id: UUID

    class Config:
        from_attributes = True
