from django.contrib import admin
from . models import Image, image, Categorie,Plan

# Register your models here.
# Register your models here.
# class AdmiBooking(admin.ModelAdmin):
#     list_display=('album','contact','create_at')

# class AdmiAlbum(admin.ModelAdmin):
#     list_display = ('title','create_at')
        

# admin.site.register(Booking, AdmiBooking)
# admin.site.register(Album, AdmiAlbum)

# admin.site.register(Booking)

class ImageAdmin(admin.ModelAdmin):
    list_display=['nom','image']

class CategorieAdmin(admin.ModelAdmin):
    list_display=['nom']

class PlanAdmin(admin.ModelAdmin):
    list_display=['titre','description','prix',]


admin.site.register(Image, ImageAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Plan, PlanAdmin)