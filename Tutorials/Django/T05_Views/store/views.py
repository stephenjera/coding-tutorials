from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page

# Create your views here.
def index(request):
    return HttpResponse('Coming soon')

def detail(request):
    return HttpResponse('details page')

@csrf_exempt
@cache_page(900)
@require_http_methods(['GET'])
def electronics(request):
    if request.method == 'GET':
        print(request.headers)
        return HttpResponse('Electronics')
    elif request.method == 'POST':
        return HttpResponseNotFound('POST method not allowed')
