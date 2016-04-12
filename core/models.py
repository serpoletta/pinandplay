from django.db import models


class Board(models.Model):
	title = models.CharField(max_length=200)
	owner = models.ForeignKey('auth.User')
	info = models.TextField(null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	is_private = models.BooleanField(null=False, default=False)


class Card(models.Model):
	author = models.ForeignKey('auth.User')
	board = models.ForeignKey('Board')
	title = models.CharField(max_length=200)
	picture = models.ImageField(null=True, upload_to="media/")  # Pillow
	info = models.TextField(null=True)
	last_edited_date = models.DateTimeField(auto_now=True)
	link = models.URLField(max_length=300)
	link_to_game = models.URLField(max_length=300)
