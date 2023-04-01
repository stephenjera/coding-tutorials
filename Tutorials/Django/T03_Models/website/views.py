from django.shortcuts import render
from .models import Member

# Create your views here.
def members(request):
    my_members = Member.objects.all().values()
    url = "website/members.html"
    context = {"my_members": my_members}
    return render(request, url, context)


def details(request, id):
    my_member = Member.objects.get(id=id)
    url = "website/details.html"
    context = {"my_member": my_member}
    return render(request, url, context)
