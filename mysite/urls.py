import os
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),                                                                                           
    path('', include('home.urls')),                                                                                           
    path('hello/', include('hello.urls')),                                                                                           
    path('accounts/', include('django.contrib.auth.urls')),
    path('autos/', include('autos.urls')),
]