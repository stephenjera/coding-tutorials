from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, "website/index.html", {"from": "from Django template"})
