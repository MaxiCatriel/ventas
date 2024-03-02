from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('log', views.log, name='log'),
    path('register/', views.register, name='register'),
    path('logout/', views.salir, name='salir'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('eventos', views.eventos, name='eventos'),
    path('eventos/crear', views.crear_evento, name='crear_evento'),
    path('eventos/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('eventos/editar/<int:id>', views.editar, name='editar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)