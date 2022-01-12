from django.contrib import admin
from .models import Listproblems, List, List2, List3, List4, List5
from .forms import List2_Forms, List3_Forms, List4_Forms, List5_Forms

admin.site.register(Listproblems)
admin.site.register(List)


@admin.register(List2)
class List2_Admin(admin.ModelAdmin):
    list_display = ('title', 'link', 'code', 'slug', 'explanation')
    form = List2_Forms

@admin.register(List3)
class List3_Admin(admin.ModelAdmin):
    list_display = ('title', 'link', 'code', 'slug', 'explanation')
    form = List3_Forms

@admin.register(List4)
class List4_Admin(admin.ModelAdmin):
    list_display = ('title', 'link', 'text' ,'code', 'slug', 'explanation')
    form = List4_Forms

@admin.register(List5)
class List5_Admin(admin.ModelAdmin):
    list_display = ('title', 'link', 'text' ,'code', 'slug', 'explanation')
    form = List5_Forms