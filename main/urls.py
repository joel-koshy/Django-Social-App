from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home), 
    path('login/', views.login_page, name='login_page'), 
    path('auth/login', views.alogin),
    path('auth/logout', views.alogout),
    path('auth/create', views.create_new_user), 
    path('signup/', views.signup_page, name='signup_page'), 
    path('me', views.user_info), 
    path('me/saved', views.saved_posts), 
    # path('posts/', views.Get_Create_Post.as_view()), 
    path('posts/', views.get_create_post, name='post_page'),
    path('posts/<int:pk>', views.get_comment_single_post, name='single_post_page'), 
    # path('posts/<int:pk>', views.Single_Post.as_view()), 
    path('posts/<int:pk>/comment', views.Comment.as_view()), 
    path('posts/<int:id>/save', views.save), 
    # path('me/saved', views.saves), 
    # path('me/followed', views.followed), 

    path('user/<int:id>', views.get_userinfo), 
    path('user/<int:id>/follow', views.follow), 

]