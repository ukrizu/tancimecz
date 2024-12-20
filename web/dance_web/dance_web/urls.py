"""dance_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('events/', views.event_list, name='events'),
    path('past-events/', views.past_events, name='past_events'),
    path('lectors/', views.lector_list, name='lectors'),
    path('search/', views.search_result, name="search"),
    path('o-tancich/', views.o_tancich, name="o_tancich"),
    path('o-nas/', views.o_nas, name="o_nas"),
    path('search_lectors/', views.search_result_lectors, name="search_lectors"),
    path('lector/<slug:slug>/', views.lector_page, name='lector_page'),
    path('event/<int:id>/', views.evening_page, name='evening_page'),
    path('workshop/<int:id>/', views.workshop_page, name='workshop_page')
] 

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)