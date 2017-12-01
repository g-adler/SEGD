from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', auth_views.login, {'template_name': 'coordenacao/login.html'}, name='index'),
    url(r'^Coordenacao$', views.index, name='pg_coord'),
    url(r'^Direcao$', views.index, name='pg_direc'),
    ]
