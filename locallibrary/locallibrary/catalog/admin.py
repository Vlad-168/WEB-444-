from django.contrib import admin
from .models import AuthorModel, BookModel, BookInstanceModel, GenreModel

# admin.site.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
	list_filter = ('first_name', 'date_of_death')

admin.site.register(AuthorModel, AuthorAdmin)
admin.site.register(BookModel)
admin.site.register(BookInstanceModel)
admin.site.register(GenreModel)
