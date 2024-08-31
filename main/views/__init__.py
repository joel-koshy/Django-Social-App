from .user import user_info, saved_posts, get_userinfo
from .post import Comment, save, get_create_post, get_comment_single_post
from .authentication import alogin, alogout, create_new_user

from django.shortcuts import render
from ..serializers import PostSerializer
from ..models import Post
from ..forms import PostForm
def home(request): 
    return render(request, "main/base.html", {})

def login_page(request): 
    return render(request, 'main/login.html', {})

def signup_page(request): 
    return render(request, 'main/signup.html', {})

# def get_posts(request): 
#     if request.method == 'POST': 
#         print(request.user)

#     queryset=Post.objects.all() 
#     serialized_posts = PostSerializer(queryset, many=True)
#     form=PostForm()
#     return render(request, 'main/post.html', {'posts': serialized_posts.data, "form": form})



