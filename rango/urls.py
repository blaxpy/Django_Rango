from django.conf.urls import url

from . import views

# app_name = 'rango'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^like_category/$', views.like_category, name='like_category'),
    url(r'^profile/(?P<username>[\w\d]+)/$', views.show_profile, name='show_profile'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^members/$', views.ShowMembersView.as_view(), name='show_members'),
    url(r'^search/$', views.search, name='search'),
    url(r'^goto/$', views.track_url, name='goto'),
    url(r'^suggest_search/$', views.suggest_search, name='suggest_search'),
    url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
]
