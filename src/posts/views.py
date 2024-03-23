from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
# Create your views here.

def post_list_and_create(request):
  # Get all of the data from the database
  qs = Post.objects.all()
  # We will use the key ('qs') in the template
  return render(request, 'posts/main.html', {'qs':qs}) 

def hello_world_view(request):
  return JsonResponse({'text': 'hello world'})