"""dj_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from uwi import views
app_name='uwi'
urlpatterns = [
    #url(r'^uwi/', include('uwi.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^terminal_data/', views.terminal_data,name='terminal_data'),
    url(r'^alerts/', views.alerts,name='alerts'),
    url(r'^info/', views.info,name='info'),
    url(r'^terminal_map/', views.terminal_map,name='terminal_map'),
]
