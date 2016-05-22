from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

    # Юзеры
    url(r'^user/$', 'core.views.user_list', name='user_list'),
    url(r'^user/(\d+)/$', 'core.views.user_profile', name='user_profile'),
    # ^user/(\d+)/edit/$
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^user_random/$', 'core.views.user_random', name='user_random'),

    # Доски
    url(r'^board/$', 'core.views.board_list', name='board_list'),
    url(r'^board/new/$', 'core.views.board_new', name='board_new'),
    url(r'^board/(?P<pk>\d+)/$', 'core.views.board_detail', name='board_detail'),
    url(r'^board/(?P<pk>\d+)/edit/$', 'core.views.board_edit', name='board_edit'),

    # Карточки
    url(r'^board/(?P<pk_board>\d+)/card/$', 'core.views.card_list', name='card_list'),
    url(r'^board/(?P<pk_board>\d+)/card/new/$', 'core.views.card_new', name='card_new'),
    url(r'^board/(?P<pk_board>\d+)/card/(?P<pk_card>\d+)/$', 'core.views.card_detail', name='card_detail'),
    url(r'^board/(?P<pk_board>\d+)/card/(?P<pk_card>\d+)/edit/$', 'core.views.card_edit', name='card_edit'),

    url(r'^$', 'core.views.index', name='index'),

]

