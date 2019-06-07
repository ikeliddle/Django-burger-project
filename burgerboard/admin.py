from django.contrib import admin


from .models import Login
from .models import Interest
from .models import Maxinterest
from .models import Mealdate

class LoginAdmin(admin.ModelAdmin):
    list_display = ('username_text', 'password_text', 'date_reg')

class InterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_applied')


admin.site.register(Login, LoginAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Maxinterest)
admin.site.register(Mealdate)