from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def my_profile_view(request):
  obj = Profile.objects.get(user=request.user)
  form = ProfileForm(request.POST or None, request.FILES or None, instance=obj)
  # Check if the request is an AJAX request
  if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    if form.is_valid():
      instance = form.save()
      return JsonResponse({
        'bio': instance.bio,
        'avatar': instance.avatar.url,
        'user': instance.user.username
      })
  context = {
    'obj': obj,
    'form': form,
  }

  return render(request, 'profiles/main.html', context)
