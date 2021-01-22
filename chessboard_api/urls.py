from django.contrib import admin
from django.urls import path, include

#import core api urls
from core.api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
]
