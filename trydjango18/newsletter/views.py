from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm


def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)

    context = {
        "title" : title,
        "form" : form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.full_name:
            instance.full_name = "Daniel"
        instance.save()
        context = {
            "title" : "Thank you",
        }

    return render(request,"home.html",context)