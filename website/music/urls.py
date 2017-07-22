from django.conf.urls import url
from . import views



app_name = 'music'

urlpatterns = [


    # /music/ListView
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^songs/$', views.SongListView.as_view(), name='song-list'),

    url(r'^search/$', views.SearchView.as_view(), name='search'),

    # /music/DetailsView
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
    # /music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    # /music/album/2
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    # /music/2/fav
    url(r'^album/(?P<pk>[0-9]+)/favorite/$', views.AlbumFavorite.as_view(), name='album-favorite'),

    url(r'^album/song/(?P<pk>[0-9]+)/songfavorite/$', views.SongFavorite.as_view(), name='song-favorite'),

    # /music/album/2/song_add
    url(r'album/(?P<pk>[0-9]+)/song/addsong/$', views.SongCreate.as_view(), name='song-add'),

    url(r'album/song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name='song-update'),
    # /music/album/2/song/delete
    url(r'album/song/(?P<pk>[0-9]+)/deletesong/$', views.SongDelete.as_view(), name='song-delete'),

    url(r'album/song/listen/(?P<pk>[0-9]+)/$', views.SongPlayer.as_view(), name='song-listen'),
]
