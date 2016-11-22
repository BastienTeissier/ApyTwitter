from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^filter/(?P<filter_name>[\w.@+-]+)/$', views.reloadIndex, name="reloadIndex"),
    url(r'^post/flag/$', views.addNewFlag, name="addNewFlag"),
    url(r'^post/filter/$', views.addNewFilter, name="addNewFilter"),
]
