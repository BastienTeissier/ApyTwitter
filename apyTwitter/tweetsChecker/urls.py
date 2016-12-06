from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^filter/(?P<filter_name>[\w.@+-]+)/$', views.reloadFilter, name="reloadFilter"),
    url(r'^filter/delete/(?P<filter_name>[\w.@+-]+)/$', views.deleteFilter, name="deleteFilter"),
    url(r'^flag/delete/(?P<flag_name>[\w.@+-]+)/$', views.deleteFlag, name="deleteFlag"),
    url(r'^post/flag/$', views.addNewFlag, name="addNewFlag"),
    url(r'^post/filter/$', views.addNewFilter, name="addNewFilter"),
    url(r'^post/search/$', views.search, name="search"),
]
