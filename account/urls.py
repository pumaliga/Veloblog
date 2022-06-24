from django.urls import path

from account.views import ListPosts, Login, Register, Logout, Profile, CreatePost, DeletePost, UpdatePost

urlpatterns = [
    path('', ListPosts.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/<int:pk>/', Profile.as_view(), name='profile'),
    path('new/post/', CreatePost.as_view(), name='new-post'),
    path('update/post/<int:pk>/', UpdatePost.as_view(), name='update-post'),
    path('delete/post/<int:pk>/', DeletePost.as_view(), name='delete-post'),

]