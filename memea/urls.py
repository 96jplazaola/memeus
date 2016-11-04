from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


app_name = 'memea'

urlpatterns = [
    # memea/
    url(r'^$', views.index, name='index'),

    # memea/id
    url(r'^(?P<meme_id>[0-9]+)/$', views.details, name='details'),

    #memea/new
    url(r'^new/$', views.memeasortu, name='memea-sortu'),


    url(r'^register/$', views.register,  name='kontua-sortu'),

    url(r'^login/$', auth_views.login, name='saioa-hasi'),

    url(r'^logout/$', auth_views.logout, {'next_page': '/memea'}, name='saioa-amaitu'),


]
