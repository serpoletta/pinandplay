from django.shortcuts import render

# Для юзеров
def user_list(request):
    return render(request, 'blog/post_list.html', {})

def user_profile(request):
    return render(request, 'blog/post_list.html', {})


# Для досок
def board_list(request):
    return render(request, 'blog/post_list.html', {})

def board_detail(request):
    return render(request, 'blog/post_list.html', {})

def board_new(request):
    return render(request, 'blog/post_list.html', {})

def board_edit(request):
    return render(request, 'blog/post_list.html', {})


# Для карточек
def card_list(request):
    return render(request, 'blog/post_list.html', {})

def card_detail(request):
    return render(request, 'blog/post_list.html', {})

def card_new(request):
    return render(request, 'blog/post_list.html', {})

def card_edit(request):
    return render(request, 'blog/post_list.html', {})

