from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
  bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':8}))
  

  class Meta:
    model = Profile
    fields = ('bio', 'avatar',)