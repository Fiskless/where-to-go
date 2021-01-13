from django.contrib import admin
from places.models import Place, Image
from django.utils.safestring import mark_safe
from django.utils.html import format_html

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ('img', 'get_preview', 'picture_number', 'place')

    def get_preview(self, obj):

        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.img.url,
            width=obj.img.width*200/obj.img.height,
            height=200,
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]


admin.site.register(Image)
