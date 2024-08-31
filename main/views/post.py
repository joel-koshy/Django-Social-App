from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Post, Comment, Save
from ..serializers import PostSerializer, SinglePostSerializer, CommentSerializer, SavedPostSerializer
from ..forms import PostForm


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_post(request): 
@api_view(['GET', 'POST'])
def get_create_post(request): 
    queryset=Post.objects.all() 
    serialized_posts = PostSerializer(queryset, many=True)
    print(request.method)
    if request.method=='POST' and request.user.is_authenticated:
        # print(request.FILES)
        data = {
            "author": request.user.id, 
            "title": request.POST.get("title"), 
            "img": request.FILES.get("img"), 
        }
        serialized_data = PostSerializer(data=data)
        # print("reached")
        if serialized_data.is_valid(): 
            # print("reached")
            serialized_data.save(); 
            # Post.objects.create(data)
            return redirect('post_page')
        else: 
            # print(serialized_data.errors)
            return Response(serialized_data.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method=='GET': 
        if request.user.is_authenticated:
            form=PostForm()
            return render(request, 'main/post.html', {'posts': serialized_posts.data, "form": form})
        else: 
            return render(request, 'main/post.html', {'posts': serialized_posts.data, "form": None})

@api_view(['GET', 'POST'])
def get_comment_single_post(request, pk): 
    if request.method == 'POST' and request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        serialized_post = PostSerializer(post)
        

        pass 
    elif request.method == 'GET': 
        pass 

class Single_Post(RetrieveUpdateAPIView): 
    # permission_classes=[IsAuthenticated]
    queryset=Post.objects.all()
    serializer_class = SinglePostSerializer

class Comment(CreateAPIView): 
    # permission_classes=[IsAuthenticated]
    queryset=Comment.objects.all()
    serializer_class = CommentSerializer

# class Save(CreateAPIView): 
#     permission_classes = [IsAuthenticated]
#     queryset = Save.objects.all()
#     serializer_class = SavedPostSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save(request, id): 
    serialized_request = SavedPostSerializer(data={'user':request.user.id, 'post_id':id})
    if not serialized_request.is_valid():
        return Response(serialized_request.errors,status.HTTP_400_BAD_REQUEST)
    
    serialized_request.save()
    return Response(serialized_request.data, status.HTTP_200_OK)






