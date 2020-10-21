from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_.urls')),
    path('', include('html_.urls')),
    path('api/', include('api.urls'))
]