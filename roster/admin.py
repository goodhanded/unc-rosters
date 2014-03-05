from django.contrib import admin
from roster.models import Player, School, Student, Sport, Team

class StudentAdmin(admin.ModelAdmin):
    search_fields = ('name',)

# Register your models here.
admin.site.register(Player)
admin.site.register(School)
admin.site.register(Student, StudentAdmin)
admin.site.register(Sport)
admin.site.register(Team)