from django.urls import path
from . import views 
urlpatterns = [
    path('me', views.user_info), 
    path('me/saved', views.saved_posts), 
    path('posts/', views.Get_Create_Post.as_view()), 
    path('posts/<int:pk>', views.Single_Post.as_view()), 
    path('posts/<int:pk>/comment', views.Comment.as_view()), 
    path('posts/<int:id>/save', views.save), 
    # path('me/saved', views.saves), 
    # path('me/followed', views.followed), 

]