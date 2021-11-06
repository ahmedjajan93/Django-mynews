from django.urls import path
from . import views

urlpatterns = [
    path('news/<int:new_id>/' , views.new_detail , name='new_detail')
]
