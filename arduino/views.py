from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

class indexs(ListView) :
    model = Post
    def get_queryset(self):
        return Post.objects.order_by('-create')


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'arduino/index.html', {'posts' : posts,})