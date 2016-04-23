from django.shortcuts import render

# Список досок юзера?
# Пагинация?
# Список некоторых рандомных досок?

# Для юзеров


def user_list(request):
    return render(request, 'blog/post_list.html', {})


def user_profile(request, pk):
    return render(request, 'blog/post_list.html', {})


# Для досок


def board_list(request):
    return render(request, 'blog/post_list.html', {})


def board_detail(request, pk):
    return render(request, 'blog/post_list.html', {})


def board_new(request):
    return render(request, 'blog/post_list.html', {})


def board_edit(request, pk):
    return render(request, 'blog/post_list.html', {})


# Для карточек


def card_list(request, pk_board):
    return render(request, 'blog/post_list.html', {})


def card_detail(request, pk_board, pk_card):
    return render(request, 'blog/post_list.html', {})


def card_new(request, pk_board):
    return render(request, 'blog/post_list.html', {})


def card_edit(request, pk_board, pk_card):
    return render(request, 'blog/post_list.html', {})

# Служебное


def index(request):
    return render(request, 'pinandplay/index.html', {}) #прописан путь о_о