from django import forms
from django.utils.translation import ugettext_lazy as ul
from django.core.exceptions import ValidationError
import datetime
from .models import BookModel

class NewBookForm(forms.ModelForm):
	class Meta:
		model = BookModel
		fields = ('__all__')

class RenewBookForm(forms.Form):
	renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks.")

	def validate_renewal_date(self):
		data = self.cleaned_data['renewal_date']

		if data < datetime.date.today():
			raise ValidationError(ul('Invalid date - date is past'))

		if data > datetime.date.today() + datetime.timedelta(weeks = 4):
			raise ValidationError(ul('Invalid date - date more than 4 weeks ahead.'))

		return data
