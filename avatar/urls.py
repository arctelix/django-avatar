from django.conf.urls import patterns, url

urlpatterns = patterns(
    'avatar.views',
    url(r'^add/$', 'add', name='avatar_add'),
    url(r'^webcam-upload/(?P<id>\d+)', 'webcam_upload', name='avatar-webcam-upload'),
    url(r'^change/$', 'change', name='avatar_change'),
    url(r'^delete/$', 'delete', name='avatar_delete'),
    url(r'^render_primary/(?P<user>[\w\d\.\-_]{3,30})/(?P<size>[\d]+)/$', 'render_primary', name='avatar_render_primary'),
    url(r'^list/(?P<username>[\+\w\@\.]+)/$', 'avatar_gallery', name='avatar_gallery'),
    url(r'^list/(?P<username>[\+\w\@\.]+)/(?P<id>[\d]+)/$', 'avatar', name='avatar'),
    url(r'^get-social-avatars/$', 'get_social_avatars', name='avatar_get_social'),
    url(r'^make/(?P<img_url>.+)/$', 'make', name='avatar_make'),
)
