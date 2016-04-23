from django.db import models


class Label(models.Model):
	""" Модель для лейблов для досок и карточек """
	title=models.CharField(max_length=30)


class Board(models.Model):
	title = models.CharField(max_length=200)
	owner = models.ForeignKey('auth.User')
	info = models.TextField(blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	is_private = models.BooleanField(null=False, default=False)		# NOT NULL - для сохранения булевой логики.
	labels = models.ManyToManyField(Label, blank=True, null=True)


class Card(models.Model):
	author = models.ForeignKey('auth.User')
	board = models.ForeignKey('Board')
	title = models.CharField(max_length=200)
	picture = models.ImageField(blank=True, null=True, upload_to="media/")
	info = models.TextField(blank=True, null=True)
	last_edited_date = models.DateTimeField(auto_now=True)
	link = models.URLField(max_length=300)
	link_to_game = models.URLField(max_length=300, blank=True, null=True)
	labels = models.ManyToManyField(Label, blank=True, null=True)
