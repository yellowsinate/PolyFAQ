from django.shortcuts import render
from .models import FAQ

def view_all_posts(request):
    questions = FAQ.objects.all()
    return render(request, 'index.html', context={'FAQ':questions})
