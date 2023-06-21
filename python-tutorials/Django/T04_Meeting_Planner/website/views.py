from django.shortcuts import render
from meetings.models import Meeting

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html", {"meetings": Meeting.objects.all()})
