"""fullcircleacupuncture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from .views import (
    home_page, 
    conditions_page, 
    services_page, 
    about_page, 
    FAQ_page,
    contact_page,
    book_appointment_page,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # CMS - Wagtail
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
    path('home/', include(wagtail_urls)),

    path('', TemplateView.as_view(template_name='home.html', extra_context={
        "instagram_profile_name": "__annagao"
    })),

    path('', home_page,name='home'),
    path('conditions/', conditions_page,name='conditions'),
    path('services/', services_page,name='services'),
    path('about/', about_page,name='about'),
    path('FAQ/', FAQ_page,name='FAQ'),
    path('contact/', contact_page,name='contact'),
    path('book-appointment/', book_appointment_page, name='book_appointment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # DEV ONLY LINE
# Development only line above handles static files... in production set up server to server from MEDIA_ROOT .. from Wagtail documentation