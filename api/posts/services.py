import uuid
from django.db.models import Count
from django.shortcuts import get_object_or_404
from posts.models import BlogPost, Comment
from posts.schemas import ListBlogPostResponse, CreateBlogPost, BlogPostResponse, CreateComment, CreateCommentResponse, CreateBlogPostResponse

class BlogPostService:
    def get_all_posts(self) -> list[ListBlogPostResponse]:
        posts = BlogPost.objects.annotate(
            n_comments=Count('comment')
        ).all()
        response = []
        for post in posts:
            response.append(
                ListBlogPostResponse.model_validate(post)
            )
        return response

    def create_blog_post(self, blog_post: CreateBlogPost) -> CreateBlogPost:
        created_post = BlogPost.objects.create(**blog_post.model_dump())
        return CreateBlogPostResponse.model_validate(created_post)
    
    def get_blog_post(self, post_id) -> BlogPostResponse:
        blog_post = get_object_or_404(BlogPost.objects.prefetch_related('comment_set'), id=post_id)
        return BlogPostResponse.model_validate(blog_post)

    def create_comment(self, post_id, comment: CreateComment):
        comment_dict = comment.model_dump()
        comment_dict["post_id"] = post_id
        created_comment = Comment.objects.create(**comment_dict)
        return CreateCommentResponse.model_validate(created_comment)