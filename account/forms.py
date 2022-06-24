from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from account.models import CustomUser, Post


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'username', 'password1', 'password2']


class CreatePostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['photo', 'title']


class UpdatePostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['photo', 'title']

