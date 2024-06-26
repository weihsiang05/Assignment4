from django.shortcuts import render
from .models import Post, Photo
from django.http import JsonResponse, HttpResponse
from .forms import PostForm
from profiles.models import Profile
from .utils import action_permission
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.

@login_required
def post_list_and_create(request):
  # Get all of the data from the database
  #qs = Post.objects.all()

  # Instance with POST data if the request method is POST
  form = PostForm(request.POST or None)
  # Check if the request is an AJAX request
  if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    if form.is_valid():
      author = Profile.objects.get(user=request.user)
      # Do want to save the form yet, this will only content the title and body. form has been defined in the forms.py
      instance = form.save(commit=False)
      # Setting the author field
      instance.author = author
      # Saving the new created object (author) and the original fields to the database
      instance.save()
      return JsonResponse({
        'title': instance.title,
        'body': instance.body,
        'author': instance.author.user.username,
        'id': instance.id
      })
  context = {
    'form': form
  }
  # We will use the key ('qs') in the template
  return render(request, 'posts/main.html', context) 

@login_required
def post_detail(request, pk):
  obj = Post.objects.get(pk=pk)
  form = PostForm()

  context = {
    'obj': obj,
    'form': form
  }

  return render(request, 'posts/detail.html', context)

@login_required
def load_post_data_view(request, num_posts):
  if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    visible = 3
    upper = num_posts
    lower = upper - visible
    size = Post.objects.all().count()

    # Get all of the data from the database
    qs = Post.objects.all() 
    data = []
    for obj in qs:
      item = {
        'id': obj.id,
        'title': obj.title,
        'body': obj.body,
        'liked': True if request.user in obj.liked.all() else False,
        'count': obj.like_count,
        'author': obj.author.user.username
      }
      data.append(item)
    return JsonResponse({'data': data[lower:upper], 'size': size})

@login_required
def post_detail_data_view(request, pk):
  obj = Post.objects.get(pk=pk)
  data={
    'id': obj.id,
    'title': obj.title,
    'body': obj.body,
    'author': obj.author.user.username,
    'logged_in': request.user.username,
  }
  return JsonResponse({'data': data})

@login_required
def like_unlike_post(request):
  # Check if the request is an AJAX request
  if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    # Get the pk form the main.js likeUnlikePosts
    pk = request.POST.get('pk')
    obj = Post.objects.get(pk=pk)
    # If the user is on that like list particular of the post
    if request.user in obj.liked.all():
      # it means that the user have already like the post
      liked = False
      # Remove the user from the like list
      obj.liked.remove(request.user)
    else:
      liked = True
      obj.liked.add(request.user)
    return JsonResponse({'like': liked, 'count': obj.like_count})
  return redirect('posts:main-board')

@login_required
@action_permission
def update_post(request, pk):
  obj = Post.objects.get(pk=pk)
  # Check if the request is an AJAX request
  if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    new_title = request.POST.get('title')
    new_body = request.POST.get('body')
    obj.title = new_title
    obj.body = new_body
    obj.save()
    return JsonResponse({
      'title': new_title,
      'body': new_body,
    })
  return redirect('posts:main-board')

@login_required
@action_permission
def delete_post(request, pk):
  obj = Post.objects.get(pk=pk)
  # Check if the request is an AJAX request
  if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    obj.delete()
    return JsonResponse({'msg': 'some message'})
  #return JsonResponse({'msg': 'access denied = ajax only'})
  return redirect('posts:main-board')
  
def image_upload_view(request):
  if request.method == 'POST':
    img = request.FILES.get('file')
    new_post_id = request.POST.get('new_post_id')
    post = Post.objects.get(id=new_post_id)
    Photo.objects.create(image=img, post=post)
  return HttpResponse()
    