from django.contrib import admin

from .models import (
    Building,
    City,
    District,
    Image,
    Neighborhood,
)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'content_type', 'object_id', 'image_tag', )
    list_display = ('name', 'image_tag', 'created',)
    readonly_fields = ('image_tag',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ('name', 'images_tag')
    list_display = ('name', 'created', )
    readonly_fields = ('images_tag', )


admin.site.register(Building)
admin.site.register(District)
admin.site.register(Neighborhood)
