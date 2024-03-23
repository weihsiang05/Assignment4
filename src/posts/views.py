from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list_and_create(request):
  # Get all of the data from the database
  qs = Post.objects.all()
  # We will use the key ('qs') in the template
  return render(request, 'posts/main.html', {'qs':qs}) 