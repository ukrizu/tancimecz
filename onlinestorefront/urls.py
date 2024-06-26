"""
URL configuration for onlinestorefront project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # all requests that start w playground/ (for ex.: playground/hello) should be handeled by the app playground and it will past the rest (for ex.: hello) to the URLconf module urls
    path('playground/', include('playground.urls')),
    path('eventlist/', include('eventlist.urls')),
    path('lectors/', include('lectors.urls')),
    path('', views.homepage),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
