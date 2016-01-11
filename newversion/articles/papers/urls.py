from django.conf.urls import url
from django.views.generic import ListView
from . import views
from .models import Tag, Author

urlpatterns = [
    url(r'^$', views.toppage, name="top"),
    url(r'^add$', views.add, name="add"),
    url(r'^delete/$', views.delete, name="delete"),
    url(r'^edit/(?P<editing_id>\d+)$', views.edit, name="edit"),
    url(r'^tags$',
        views.tag_list, name="tags"),
    url(r'^tags/delete$', views.delete_tag, name="del-tag"),
    url(r'^tag/(?P<tag_id>\d+)$', views.tag, name="tag"),
    url(r'^authors',
        ListView.as_view(model=Author,
                         template_name="author_list.html"),
        name="authors")
]
