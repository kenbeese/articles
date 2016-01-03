from django.conf.urls import url
from django.views.generic import ListView
from . import views
from .models import Tag

urlpatterns = [
    url(r'^$', views.toppage, name="top"),
    url(r'^add$', views.add, name="add"),
    url(r'^delete/$', views.delete, name="delete"),
    url(r'^edit/(?P<editing_id>\d+)$', views.edit, name="edit"),
    url(r'^tags$', ListView.as_view(model=Tag, template_name="tag_list.html"))
]
