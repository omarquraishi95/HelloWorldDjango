#Import Django HTTP
from django.http import HttpResponse

#Return Message
def index(request):
    return HttpResponse("Hello World!")
