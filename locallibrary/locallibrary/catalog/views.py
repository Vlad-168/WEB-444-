from django.shortcuts import render
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
	
