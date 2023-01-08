from . import views, api
from django.urls import path
urlpatterns = [
path('', views.index, name='home'),
 path('index.html', views.index, name='home'),
 path('Tables.html', views.dht11, name='data'),
 path('api/list', api.Dlist, name='DHT11List'),
 # genericViews
 path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
 path('charts.html', views.charts, name='charts'),
]
