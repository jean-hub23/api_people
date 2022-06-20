from django.contrib import admin
from rest_framework import permissions
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# VARIABLE CREADA PARA EL SWAGGER
schema_view = get_schema_view(

   openapi.Info(
      title="Documentacion API",
      default_version='v0.1',
      description="Documentacion para la API de Movimientos",
      terms_of_service="https://www.facebook.com/jecachusa",
      contact=openapi.Contact(email="jecachusa.1996@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),

   public=True,
   permission_classes=[permissions.AllowAny],

)


urlpatterns = [


    path('admin/', admin.site.urls),

    # URL APP
    path('movimientos/', include('apps.movimientos.api.routers')),
    path('autorizantes/', include('apps.autorizantes.api.routers')),
    path('motivos/', include('apps.motivos.api.routers')),
    path('areas/', include('apps.areas.api.routers')),
    path('detalle-personal/', include('apps.detalle_personal.api.routers')),

    # URLS THIRD
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

# SE ADICIONÓ EL METODO PARA SWAGGER
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]