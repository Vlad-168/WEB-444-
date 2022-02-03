from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .models import BookModel, BookInstanceModel, AuthorModel
from .forms import NewBookForm, RenewBookForm

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

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
	book_instance = get_object_or_404(BookInstanceModel, pk = pk)

	if request.method == 'POST':
		form = RenewBookForm(request.POST)

		if form.is_valid():
			book_instance.due_back = form.cleaned_data['renewal_date']
			book_instance.save()
			return HttpResponseRedirect(reverse('index'))
			
	else: #GET
		proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks = 3)
		form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

	return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'book_instance':book_instance,})


	