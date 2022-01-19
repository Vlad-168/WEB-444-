from django.db import models
from django.urls import reverse
import uuid

class BookModel(models.Model):
	title = models.CharField(max_length=200) 
	author = models.ForeignKey('AuthorModel', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text='Краткое содержание книги')
	isbn = models.CharField('ISBN', max_length=13, unique=True)
	genre = models.ManyToManyField('GenreModel', help_text='Выберите жанр')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('index')

class BookInstanceModel(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Уникальный идентификатор книги')
	book = models.ForeignKey('BookModel', on_delete=models.RESTRICT, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = {
		('m', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	}
	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text='Статус книги',
		)
	class Meta:
		ordering=['due_back']

	def get_absolute_url(self):
		return reverse('index')

	def __str__(self):
		return f'{self.id} ({self.book.title})'


class GenreModel(models.Model):
	name = models.CharField(max_length=200, help_text='Введите жанр книги')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('index')


class AuthorModel(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('index')#, args=[str(self.id)])

	def __str__(self):
		return f'{self.last_name}, {self.first_name}'
	