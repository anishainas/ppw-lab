"""Lab1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
import lab_1.urls as lab_1
import lab_2.urls as lab_2
import lab_2_addon.urls as lab_2_addon
import lab_3.urls as lab_3
import lab_4.urls as lab_4
import lab_5.urls as lab_5
import lab_6.urls as lab_6
import lab_7.urls as lab_7
import lab_8.urls as lab_8
import lab_9.urls as lab_9
import lab_10.urls as lab_10
from lab_1.views import index as index_lab1
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^lab-1/', include(lab_1,namespace='lab-1')),
    url(r'^lab-2/', include(lab_2,namespace='lab-2')),
    url(r'^lab-2-addon/', include(lab_2_addon,namespace='lab_2_addon')),
    url(r'^lab-3/', include(lab_3,namespace='lab-3')), 
    url(r'^lab-4/', include(lab_4, namespace='lab-4')),
    url(r'^lab-5/', include(lab_5, namespace='lab-5')),
    url(r'^lab-6/', include(lab_6, namespace='lab-6')),
    url(r'^lab-7/', include(lab_7, namespace='lab-7')),
    url(r'^lab-8/', include(lab_8, namespace='lab-8')),
    url(r'^lab-9/', include(lab_9, namespace='lab-9')),
    url(r'^lab-10/', include(lab_10, namespace='lab-10')),
    url(r'^$', RedirectView.as_view(url='lab-8/', permanent=True))
]
