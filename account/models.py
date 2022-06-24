from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='users/', default='default.jpeg')

    def get_avatar(self):
        if self.avatar == 'default.jpeg':
            return 'media/users/default.jpeg'
        return f'media/{self.avatar}'


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='workouts')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    title = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']



