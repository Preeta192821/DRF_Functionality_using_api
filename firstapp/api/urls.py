from django.conf.urls import url
from .views import hello_world


urlpatterns =[

    url('first',hello_world)
]