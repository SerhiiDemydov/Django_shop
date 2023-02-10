from django.contrib import admin

# Register your models here.
from products.models import Product, PublishingHouse, GameType


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'publishing_house')
    autocomplete_fields = ('publishing_house',)


class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'display_games_count')
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate_games_count()

    def display_games_count(self, obj):
        return obj.games_count


admin.site.register(Product, ProductAdmin)
admin.site.register(PublishingHouse, PublishingHouseAdmin)
admin.site.register(GameType, )
