from django.contrib import admin
from .models import Art, ArtCategory, Painter, ArtImage

# Register your models here.
@admin.register(Art)
class BookModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    

admin.site.register(ArtCategory)
admin.site.register(Painter)

admin.site.register(ArtImage)