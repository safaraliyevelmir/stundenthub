from django.db import models
from django.contrib.auth import get_user_model
from main.models import Tag

User = get_user_model()


class Club(models.Model):

    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    users = models.ManyToManyField(User,blank=True,related_name='club_users')
    title = models.CharField(max_length=255,unique=True)
    description = models.CharField(max_length=255)
    is_private = models.BooleanField(default=True)
    image = models.ImageField(upload_to='club/')
    tags = models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return self.title
    

class ClubPost(models.Model):

    title = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
