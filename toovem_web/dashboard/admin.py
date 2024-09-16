from django.contrib import admin
from .models import Donor

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'status', 'category')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('status', 'category', 'nationality', 'menstrual_cycle_type')
    ordering = ('-date_of_birth',)


from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import Donor

class DonorAdmin(ModelAdmin):
    model = Donor
    menu_label = 'Donors'  # Name in the sidebar
    menu_icon = 'user'  # Icon (from Wagtail's available icons)
    list_display = ('first_name', 'last_name', 'email', 'status', 'category')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('status', 'category', 'nationality', 'menstrual_cycle_type')
    ordering = ('-date_of_birth',)

modeladmin_register(DonorAdmin)