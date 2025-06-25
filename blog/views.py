from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion
from .models import Fotografía
from django.contrib.auth.models import User


def lista_public(request): 
    publicaciones=Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    
    usr_id=request.GET.get('usuario')
    if usr_id:
        publicaciones=publicaciones.filter(autor_id=usr_id)
    usuarios=User.objects.all()
    if usr_id:
        usuario_activo=int(usr_id)
    else:
        usuario_activo=None

    return render(request, 'blog/lista_public.html', {
        'publicaciones': publicaciones,
        'usuarios': usuarios,
        'usuario_activo': usuario_activo
    })
def lista_fotografía(request):
    Fotografías = Fotografía.objects.all()
    return render(request, 'blog/lista_fotografía.html', 
    {'Fotografías': Fotografías})
# Create your views here.
