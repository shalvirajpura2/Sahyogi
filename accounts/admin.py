from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Event, Application
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'user_type', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'phone_number', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type', 'phone_number', 'bio')}),
    )

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'recruiter', 'created_at')
    list_filter = ('date', 'location')
    search_fields = ('title', 'description', 'location')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('volunteer', 'event', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('volunteer__username', 'event__title')

admin.site.register(CustomUser, CustomUserAdmin) 