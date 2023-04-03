from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
from django.forms import modelform_factory

# Create your views here.
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms(request):
    return render(request, "meetings/rooms.html", {"rooms": Room.objects.all()})


# This is a class
MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == "POST":
        # Form has been submitted
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
