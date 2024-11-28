from django.contrib import admin
from account.models import Profile

# Register your models here.
admin.site.register(Profile)

class Profile(admin.ModelAdmin):
    list_display=('staff','adress','phone')