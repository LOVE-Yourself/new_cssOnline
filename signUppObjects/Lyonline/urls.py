"""Lyonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve


from Lyonline.settings import MEDIA_ROOT
import xadmin
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^users/',include('users.urls',namespace='user')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^$',TemplateView.as_view(template_name='index.html'),name='index'),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$',serve,{'document_root':STATIC_ROOT}),
    url(r'^course/',include('course.urls',namespace='course')),
    url(r'^pay/',include('tradApp.urls',namespace='alipay')),
    url(r'^operation/',include('operation.urls',namespace='operation')),

]

handler404 = 'users.views.page_not_found'