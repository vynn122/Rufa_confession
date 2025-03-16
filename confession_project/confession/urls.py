from django.urls import path
from .views import confession_submit

urlpatterns = [
    path('', confession_submit, name='confession_form'),
    # path('success/', confession_success, name='confession_success'),
]