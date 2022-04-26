from django.test import TestCase

from catalog.models import AuthorModel as Author

class YourTestClass(TestCase):

	@classmethod
	def setUpTestData(cls):
		Author.objects.create(first_name="Ivan", last_name="Ivanov")
		print("Author was created.")

	def setUp(self):
		print("setUp: Running")
		pass

	def tearDown(self):
		print("tearDown: Running")
		pass

	def test_max_length_first_name(self):
		author = Author.objects.get(id=1)
		field_length = author._meta.get_field('first_name').max_length 
		return self.assertEquals(field_length, 100)

	def test_field_label_first_name(self):
		author = Author.objects.get(id=1)
		field_label = author._meta.get_field('first_name').verbose_name 
		return self.assertEquals(field_label, 'first name')

		# Author model tests:
		# 1) Протестировать max_length для поля last_name
		# 2) Протестировать max_length для поля last_name со значением 120
		# 3) Протестировать verbose_name для first_name ('first name')
		# 4) Протестировать verbose_name для last_name ('last name')
		# 5) Протестировать метод get_absolute_url() для author (Удостовериться, что мы получаем автора с id = 1)
		#
		# Book model tests:
		# 1) Протестировать max_length для поля title (200)
		# 2) Протестировать on_delete для поля author (models.SET_NULL)
		# 3) Протестировать help_text для поля summary ('Краткое содержание книги')
		# 4) Протестировать verbose_name для поля isbn ('ISBN')
		# 5) Протестировать verbose_name для поля genre ('GenreModel')