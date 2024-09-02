from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from django.shortcuts import render
from django.contrib.auth.models import User
from ..models import Follow, Post, Save
from ..serializers import UserSerializer, SavedPostSerializer, FollowSerializer

from django.shortcuts import get_object_or_404


def get_userinfo(request, id): 
    user_info = get_object_or_404(User, pk=id)
    serialized_info = UserSerializer(user_info)
    is_following = Follow.objects.filter(user=id, follower=request.user.id).exists() 
    following = Follow.objects.filter(follower=id)
    serialized_following = FollowSerializer(following, many=True)
    return render(request, 'main/user.html', {"data": serialized_info.data, "is_following":is_following, "following":serialized_following.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request): 
    item = get_object_or_404(User, username=request.user )
    serialized_item = UserSerializer(item)
    return Response(serialized_item.data, status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saved_posts(request): 
    posts = Save.objects.filter(user_id=request.user.id)
    serialized_posts = SavedPostSerializer(posts, many=True)
    return Response(serialized_posts.data, status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_posts(request): 
    post_id = request.data.get("post_id")
    selected_post = Save.objects.filter(user_id=request.user.id, post_id=post_id)
    selected_post.delete()
    return Response({"message": "Item Deleted Succesfully"}, status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'DELETE'])
def follow(request, id):
    if request.method == 'POST': 
        data = {
            "user":id, 
            "follower":request.user.id
        }
        serialized_request = FollowSerializer(data = data )
        if not serialized_request.is_valid():
            return Response(serialized_request.errors, status.HTTP_400_BAD_REQUEST)
        
        serialized_request.save() 
        return Response(serialized_request.data, status.HTTP_200_OK)
    elif request.method == 'DELETE': 
        selected_item = get_object_or_404(Follow, user=id, follower=request.user.id)
        selected_item.delete() 
        return Response(status.HTTP_204_NO_CONTENT)