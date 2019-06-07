from django.contrib import admin

from .models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('blog_name', 'quote_text')

admin.site.register(Quote, QuoteAdmin)