"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from juegos import views as Game_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion API",
      default_version='v0.1',
      description="documentacion de api de catalogo de juegos",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="alexischavez1911@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



# Api router
router = routers.DefaultRouter()
router.register('games-detail', Game_views.GameViewSet, basename='games_detail'),


urlpatterns = [
    #rutas de documentacion
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Admin routes
    path('admin/', admin.site.urls),
    # Api routes
    path('api/', include('authentication.urls')),
    path('api/', include(router.urls)),
    path('api/',include('juegos.urls')),
    
]

# servidor de archivos estaticos
if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)