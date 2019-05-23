from django.conf.urls import url, include
from . import views

app_name = 'app1'

urlpatterns = [
url('^$', views.index_view, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url('^profile/', views.profile, name='profile'),
    url(r'^details/(?P<pk>[0-9]+)/$', views.detail_view, name='details'),
    url(r'^results/', views.search_view, name='search'),
]