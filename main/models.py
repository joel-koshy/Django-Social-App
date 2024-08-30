from typing import Iterable
from django.db import models
# from .supabase_storage import SupabaseStorage
# Create your models here.
from django.dispatch import receiver
from django.contrib.auth.models import User 

import boto3
import environ 

env = environ.FileAwareEnv()
environ.Env.read_env()

client = boto3.client('s3', aws_access_key_id=env('BUCKET_ACCESS_KEY'),aws_secret_access_key=env('BUCKET_SECRET_ACCESS_KEY'), endpoint_url=env('BUCKET_ENDPOINT_URL'), region_name='us-east-1')

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    likes = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/', blank=True, null=True)

    @receiver(models.signals.pre_delete, sender='main.Post')
    def delete_bucket_img(sender, instance, **kwargs): 
        for field in instance._meta.fields: 
            if field.name == "img": 
                img_location = getattr(instance, field.name).url
                # print(img_location)
                img_key = img_location[74:] #65 length of custom domain
                print("IMAGE KEY: "+img_key)
                response = client.delete_object(Bucket='images', Key=img_key)

    def __str__(self) -> str:
        return self.title 


class Comment(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self) -> str:
        return ("Comment by User ID: " + self.user + "on Post ID: " + self.post)
 

class Save(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return ("User ID: " + self.user + "liked Post ID: " + self.post)
    

class Follow(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    follower = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta: 
        unique_together = (('user'), ('follower'))

    def __str__(self) -> str:
        return ("User ID: " + self.user + "follows User ID: " + self.follower)
 



