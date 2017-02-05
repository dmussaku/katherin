from django.contrib import admin

from .models import (
    Building,
    City,
    District,
    Neighborhood,
)


# @admin.register(City)
# class CityAdmin(admin.ModelAdmin):
#     fields = ('name', 'images_tag')
#     list_display = ('name', 'created', )
#     readonly_fields = ('images_tag', )


admin.site.register(Building)
admin.site.register(District)
admin.site.register(Neighborhood)
