from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

# Register your models here.


class ytuber(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}"  width="40" />', format(object.photo.url))

    list_display = ('id', 'myphoto', 'fullname','is_featured',)
    list_display_links = ('id', 'myphoto', 'fullname',)
    search_fields = ('fullname', )
    list_filter = ('city', 'category')


admin.site.register(Youtuber, ytuber)
