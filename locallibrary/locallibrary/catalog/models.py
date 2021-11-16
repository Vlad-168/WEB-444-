from django.db import models
import uuid

class BookModel(models.Model):
	title = models.CharField(max_length=200)
	# TODO Need uncommented when you added AuthorModel table 
	# author = models.ForeignKey('AuthorModel', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text='Краткое содержание книги')
	isbn = models.CharField('ISBN', max_length=13, unique=True)
	# TODO Need uncommented when you added GenreModel table 
	# genre = models.ManyToManyField('GenreModel', help_text='Выберите жанр')

	def __str__(self):
		return self.title

class BooxInstanceModel(models.Model):
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

	def __str__(self):
		return f'{self.id} ({self.book.title})'


class GenreModel(models.Model):


class AuthorModel(models.Model):

		
	
		