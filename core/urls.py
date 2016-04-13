from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', 'views.home', name='home'),
    # Юзеры
    url(r'^user/$', 'views.user_list', name='user_list'),
    url(r'^user/(\d+)/$', 'views.user_profile', name='user_profile'),
    # ^user/(\d+)/edit/$

    # Доски
    url(r'^board/$', 'views.board_list', name='board_list'),
    url(r'^board/new/$', 'views.board_new', name='board_new'),
    url(r'^board/(\d+)/$', 'views.board_detail', name='board_detail'),
    url(r'^board/(\d+)/edit/$', 'views.board_edit', name='board_edit'),

    # Карточки
    url(r'^board/(\d+)/card/$', 'views.card_list', name='card_list'),
    url(r'^board/(\d+)/card/new/$', 'views.card_new', name='card_new'),
    url(r'^board/(\d+)/card/(\d+)/$', 'views.card_detail', name='card_detail'),
    url(r'^board/(\d+)/card/(\d+)/edit/$', 'views.card_edit', name='card_edit'),
]

