from django.contrib import admin
from .models import Note
# Register your models here.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    '''
        Admin View for Note
    '''
    list_display = ('id', 'title', 'slug', 'created')
    list_filter = ('created',)
    search_fields = ('title', 'created')
