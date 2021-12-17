from django.urls import path
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from shedule.views import *

urlpatterns = [
    path('', lambda request: redirect(reverse_lazy('create'))),
    path('admin/', admin.site.urls),
    path('shedule/', generate_shedule, name='create'),
]

