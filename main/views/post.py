from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from ..models import Post, Comment, Save
from ..serializers import PostSerializer, SinglePostSerializer, CommentSerializer, SavedPostSerializer

class Get_Create_Post(ListCreateAPIView): 
    # permission_classes=[IsAuthenticated]
    queryset=Post.objects.all()
    serializer_class = PostSerializer

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






