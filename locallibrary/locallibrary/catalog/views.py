from django.shortcuts import render
from django.views.generic import CreateView
from .models import BookModel, BookInstanceModel, AuthorModel
from .forms import NewBookForm

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
	fields = ('__all__')
	
# class BookCreateView(CreateView):
# 	model = BookModel
# 	fields = ('__all__')

def new_book(request):
	form = NewBookForm()
	return render(request, 'catalog/bookmodel_form.html', {'form': form}) 
	