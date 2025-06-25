from django.contrib import admin
from .models import Publicacion
from .models import Fotografía


admin.site.register(Publicacion)
admin.site.register(Fotografía)