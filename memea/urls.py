from django.conf.urls import url
from . import views

app_name = 'memea'

urlpatterns = [
    # memea/
    url(r'^$', views.index, name='index'),

    # memea/id
    url(r'^(?P<meme_id>[0-9]+)/$', views.details, name='details'),

    #memea/new
    url(r'^new/$', views.memeasortu, name='memea-sortu'),


    url(r'^register/$', views.register,  name='kontua-sortu'),


]
