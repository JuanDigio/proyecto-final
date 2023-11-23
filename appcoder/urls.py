
from django.urls import path
from django.http import HttpResponse

def view_inicio(xx):
    return HttpResponse("bienvenidos")


urlpatterns = [
    path("inicio/", view_inicio ),
]
