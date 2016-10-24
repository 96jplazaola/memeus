from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # memea/
    url(r'^$', views.index, name='index'),

    # memea/id
    url(r'^(?P<meme_id>[0-9]+)/$', views.details, name='details')
]
