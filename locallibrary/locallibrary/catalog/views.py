from django.shortcuts import render
from django.views.generic import CreateView
from .models import BookModel, BookInstanceModel, AuthorModel

def index(request):
	num_books = BookModel.objects.all().count()
	num_instances = BookInstanceModel.objects.all().count()
	num_instances_available = BookInstanceModel.objects.filter(status='a')
	num_authors = AuthorModel.objects.all().count()

	return render(
		request,
		'index.html',
		context={
			'num_books': num_books,
			'num_instances': num_instances,
			'num_instances_available': num_instances_available,
			'num_authors': num_authors,
		})

class AuthorCreateView(CreateView):
	model = AuthorModel
	fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
	
