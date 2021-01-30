from django.contrib import admin
from places.models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin
from django.utils.html import format_html
import traceback


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):

    model = Image
    extra = 0
    readonly_fields = ['get_preview']
    fields = ('order', 'img', 'get_preview', 'place')

    def get_preview(self, obj):

        try:
            return format_html('<img src="{}" height={} />',
                               obj.img.url,
                               200,
                               )
        except ValueError:
            return "There will be a preview when you choose file"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
    search_fields = ['title']


admin.site.register(Image)
