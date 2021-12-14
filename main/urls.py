from django.urls import path
from django.contrib import admin

from shedule.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shedule/', generate_shedule, name='create'),
]

