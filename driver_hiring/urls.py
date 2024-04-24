"""driver_hiring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from hiring_app.views import Index_View, user_registration, driver_registration

from hiring_app import admin_urls, user_urls, driver_urls, staff_urls

urlpatterns = [
    path('admin/',admin_urls.urls()),
    path('user/',user_urls.urls()),
    path('driver/',driver_urls.urls()),
    path('staff/',staff_urls.urls()),

    path('',Index_View.as_view()),
    path('user_registration',user_registration.as_view()),
    path('driver_registration',driver_registration.as_view()),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
