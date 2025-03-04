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
        print(request.FILES)
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
        data={
            "user":request.user.id, 
            "post":pk, 
            "content":request.POST.get("content")
        }
        deserialized_comment_data = CommentSerializer(data=data)
        if deserialized_comment_data.is_valid(): 
            deserialized_comment_data.save()
            return Response(status.HTTP_200_OK)
        else: 
            return Response(status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET': 
        post = get_object_or_404(Post, pk=pk)
        serialized_post = SinglePostSerializer(post)
        # print(serialized_post.data)
        return render(request, 'main/single_post.html', {'post':serialized_post.data})

class Comment(CreateAPIView): 
    # permission_classes=[IsAuthenticated]
    queryset=Comment.objects.all()
    serializer_class = CommentSerializer

# class Save(CreateAPIView): 
#     permission_classes = [IsAuthenticated]
#     queryset = Save.objects.all()
#     serializer_class = SavedPostSerializer

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def save(request, id): 
    # print(request.body)
    if request.method == 'POST': 

        data = {
            "user":request.user.id, 
            "post_id":id, 
        }    
        if Save.objects.filter(user=request.user.id, post=id).exists(): 
            return Response({"message": "Post already Saved"}, status.HTTP_200_OK)

        serialized_request = SavedPostSerializer(data=data)
        if not serialized_request.is_valid():
            return Response(serialized_request.errors,status.HTTP_400_BAD_REQUEST)
        
        serialized_request.save()

        return Response( status.HTTP_200_OK)
    elif request.method == 'DELETE': 
        selected_item = get_object_or_404(Save, user=request.user.id, post=id )
        selected_item.delete()
        return Response(status.HTTP_204_NO_CONTENT)







