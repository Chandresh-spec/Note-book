from django.contrib import admin
from .models import Note
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display=('title','created_at')
    search_fields=('title','content')
    list_display=('created_at',)
    ordering=('created_at',)


admin.site.register(Note,NoteAdmin)
    

   
