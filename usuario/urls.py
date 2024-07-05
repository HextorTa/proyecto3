from django.urls import path
from .views import Pagina1, Pagina2, Pagina3, Pagina4, Pagina5, Pagina6, registrar

urlpatterns = [
    path('', Pagina1, name= 'Pagina1'),
    path('registrar/',registrar),
    path('Pagina2/', Pagina2, name= 'Pagina2'),
    path('Pagina3/', Pagina3, name= 'Pagina3'),
    path('Pagina4/', Pagina4, name= 'Pagina4'),
    path('Pagina5/', Pagina5, name= 'Pagina5'),
    path('Pagina6/', Pagina6, name= 'Pagina6'),
]
