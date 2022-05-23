from idlelib.textview import view_file

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_view, name='post list view')
]