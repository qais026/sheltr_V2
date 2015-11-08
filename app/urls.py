from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
    url(r'^blog', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^search/$', views.search, name='search'),
    url(r'^results/$', views.results, name='results'),                                                                                   
    url(r'^app/category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^about/$', views.about, name="about"),
    url(r'^(?i)PHC/$', views.PHC, name="PHC"),
    url(r'^$', views.home, name='home'),) # case insensitive regex for PHC
