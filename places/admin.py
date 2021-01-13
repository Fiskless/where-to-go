from django.contrib import admin
from places.models import Place, Image
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin

# Register your models here.

class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ['get_preview']
    fields = ('my_order', 'img', 'get_preview', 'place')

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
