from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import House, Entrance, Apartment

class EntranceInline(admin.TabularInline):
    model = Entrance
    extra = 1


class ApartmentInline(admin.TabularInline):
    model = Apartment
    extra = 1


@admin.register(House)
class HouseAdmin(MPTTModelAdmin):
    inlines = [EntranceInline]


@admin.register(Entrance)
class EntranceAdmin(admin.ModelAdmin):
    inlines = [ApartmentInline]


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['apartment_number', 'floor_number', 'num_of_rooms', 'entrance']