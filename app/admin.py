from django.contrib import admin
from app.models import JobPost, Location, Author, Skills


class jobadmin(admin.ModelAdmin):
    list_display= ('__str__', 'title', 'salary', 'date',)
    list_filter=('salary', 'date', 'expiry',)
    search_fields=('title', 'salary',)
    search_help_text='Write your search query'
    # fields= (('title', 'description'), 'expiry')
    # exclude= ('description',)

    fieldsets= (('basic_info', {'fields':('title', 'description')}),
                 ('more info', {'classes': ('collapse','wide',),
                                'fields':(('salary', 'expiry'), 'slug')}),)
    

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Skills)
admin.site.register(Author)