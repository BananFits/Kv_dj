from django.contrib import admin
from .models import humster
from .models import Favourite_book


@admin.register(humster)
class HumsterAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'time_create', 'is_published', 'brief_info')
    list_display_links = ('title',)
    list_editable = ('content',)
    search_fields = ['title']
    list_filter = ['is_published']

    @admin.display(description="Краткое описание")
    def brief_info(self, humster: humster):
        return f"Описание {len(humster.content)} символов."




@admin.register(Favourite_book)
class Favourite_bookAdmin(admin.ModelAdmin):
    list_display = ('title', 'interesting', 'brief_info')
    list_display_links = ('interesting', )
    list_editable = ('title',)

    @admin.display(description="Краткое описание")
    def brief_info(self, humster: Favourite_book):
        return f"Описание {len(humster.slug)} символов."

#admin.site.register(HumsterAdmin)
#admin.site.register(Favourite_bookAdmin)
