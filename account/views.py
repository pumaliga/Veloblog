from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from account.forms import RegistrationForm, CreatePostForm, UpdatePostForm
from account.models import CustomUser, Post


class Login(LoginView):
    template_name = 'login.html'


class Register(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = '/'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = reverse_lazy('login')


class ListPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'index.html'
    login_url = 'login/'


class Profile(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile.html'
    login_url = 'login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.request.user)
        return context


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    template_name = 'new_post.html'
    success_url = '/'
    login_url = 'login/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form=form)


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return f"/profile/{self.request.user.pk}/"


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'

    def get_success_url(self):
        return f"/profile/{self.request.user.pk}/"
