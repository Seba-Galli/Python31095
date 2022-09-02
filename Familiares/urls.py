from django.urls import path
from Familiares.views import familia, familia1, familia2

urlpatterns = [
    path('novia/', familia),
    path('madre/', familia1),
    path('hermano/', familia2),
]