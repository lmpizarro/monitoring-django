from django.contrib import admin

# Register your models here.

from app.models import MeetUP, Meeter


@admin.register(MeetUP)
class MeetUpAdmin(admin.ModelAdmin):
    list_display = ['name', 'meet_date']

@admin.register(Meeter)
class MeeterAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']