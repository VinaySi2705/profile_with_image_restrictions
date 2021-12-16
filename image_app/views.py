from django.shortcuts import render, redirect
from .models import Profile
from .forms import UserForm

# Create your views here.
def index(request):
    form = UserForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect(display_url)
    else:
        form = UserForm()

    return render(request, "image_app/cover.html" , {'form':form})


def display_url(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        return render(request, "image_app/display_url.html", {'profiles':profiles})
