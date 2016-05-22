from django.shortcuts import render
from .models import Board
from django.contrib.auth.decorators import login_required
from extuser.models import ExtUser

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Список досок юзера?
# Пагинация?
# Список некоторых рандомных досок?

# Для юзеров


def user_list(request):
    return render(request, 'blog/post_list.html', {})

def user_profile(request, pk):
    user = ExtUser.objects.filter(pk=pk)
    boards = Board.objects.filter(owner=pk)
    return render(request, 'pinandplay/user_profile.html', {'user':user, 'boards': boards})

@login_required
def home(request):
    return HttpResponseRedirect(
               reverse(user_random(),
                       args=[request.user.pk]))

@login_required
def user_random(request, pk):
    user = ExtUser.objects.filter(pk=pk)
    boards = Board.objects.all()[:15]
    return render(request, 'pinandplay/user_random.html', {'user':user, 'boards': boards})

# Для досок


def board_list(request):
    return render(request, 'blog/post_list.html', {})


def board_detail(request, pk):
    return render(request, 'pinandplay/board.html', {})

@login_required
def board_new(request):
    return render(request, 'blog/post_list.html', {})

@login_required
def board_edit(request, pk):
    return render(request, 'blog/post_list.html', {})


# Для карточек


def card_list(request, pk_board):
    return render(request, 'blog/post_list.html', {})


def card_detail(request, pk_board, pk_card):
    return render(request, 'pinandplay/card.html', {})

@login_required
def card_new(request, pk_board):
    return render(request, 'blog/post_list.html', {})

@login_required
def card_edit(request, pk_board, pk_card):
    return render(request, 'blog/post_list.html', {})

# Служебное


def index(request):
    return render(request, 'pinandplay/index.html', {})