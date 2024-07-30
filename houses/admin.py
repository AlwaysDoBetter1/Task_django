from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import House, Entrance, Apartment
from .models import Notifications

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

@admin.register(Notifications)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('user__username', 'message')
