from django.conf.urls import patterns, url

urlpatterns = patterns('followers.views',
    url(r'^followers/(?P<username>[a-zA-Z0-9_-]+)/$', 'friend_list', {
        'list_type': 'followers'
    }, name='followers_followers'),
    url(r'^following/(?P<username>[a-zA-Z0-9_-]+)/$', 'friend_list', {
        'list_type': 'following'
    }, name='followers_following'),
    url(r'^mutual/(?P<username>[a-zA-Z0-9_-]+)/$', 'friend_list', {
        'list_type': 'mutual'
    }, name='followers_mutual'),
    url(r'^follow/(?P<username>[a-zA-Z0-9_-]+)/$', 'follow',
        name='followers_follow'),
    url(r'^unfollow/(?P<username>[a-zA-Z0-9_-]+)/$', 'unfollow', 
        name='followers_unfollow'),
)
