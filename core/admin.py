"""
Admin configuration for Code Vimarsh models.
"""
from django.contrib import admin
from .models import Event, TeamMember


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin interface for Event model."""
    list_display = ['title', 'date', 'created_at']
    list_filter = ['date', 'created_at']
    search_fields = ['title', 'description']
    date_hierarchy = 'date'


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    """Admin interface for TeamMember model."""
    list_display = ['name', 'role', 'photo', 'created_at']
    list_filter = ['role', 'created_at']
    search_fields = ['name', 'role', 'bio']
    fields = ['name', 'role', 'photo', 'bio']

