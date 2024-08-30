from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from django.contrib.auth.models import User
from ..models import Follow, Post, Save
from ..serializers import UserSerializer, SavedPostSerializer

from django.shortcuts import get_object_or_404

# class User(generics.ListAPIView): 
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

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
    return Response({"message": "Item Deleted Succesfully"}, status.HTTP_204_NO_CONTENTp)