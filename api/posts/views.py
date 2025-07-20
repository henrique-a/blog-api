from django.shortcuts import render
from ninja import NinjaAPI

from posts.schemas import ListBlogPostResponse, CreateBlogPost, BlogPostResponse, CreateComment, CreateCommentResponse, CreateBlogPostResponse
from posts.services import BlogPostService

# Create your views here.
api = NinjaAPI()
blog_post_service = BlogPostService()

@api.post("/{id}/comments", response=CreateCommentResponse)
def create_comment(request, id: str, payload: CreateComment):
    blog_post = blog_post_service.create_comment(id, payload)
    return blog_post

@api.get("/{id}", response=BlogPostResponse)
def get_post(request, id: str):
    blog_post = blog_post_service.get_blog_post(id)
    return blog_post


@api.get("/", response=list[ListBlogPostResponse])
def get_posts(request):
    blog_posts = blog_post_service.get_all_posts()
    return blog_posts

@api.post("/", response=CreateBlogPostResponse)
def create_post(request, payload: CreateBlogPost):
    created_post = blog_post_service.create_blog_post(payload)
    return created_post


