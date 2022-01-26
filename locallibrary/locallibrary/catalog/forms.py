from django import forms

from .models import BookModel

class NewBookForm(forms.ModelForm):
	class Meta:
		model = BookModel
		fields = ('__all__')