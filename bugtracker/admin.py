# coding: utf-8
from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('closed', 'title', 'text', 'created', 'user')
    list_filter = ['created', 'closed']
    search_fields = ['title', 'text']
    actions = ['change_to_closed']

    def change_to_closed(self, request, queryset):
        queryset.update(closed = True)
    change_to_closed.short_description = u'пометить как решенные'

#admin.site.register(Ticket, TicketAdmin)
