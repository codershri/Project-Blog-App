from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import post

# Create your views here.

def home(request):
    context={
        'posts': post.objects.all()


    }
    return render(request, 'Blog_App/home.html',context)

class PostListView(ListView):
    model = post
    template_name = 'Blog_App/home.html' ## <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    context={
        'title': 'About'
    }
    return render(request, 'Blog_App/about.html',context)