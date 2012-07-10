from django.contrib import admin
from nonprofit.staff.models import Location, Department, Member


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Location, LocationAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Department, DepartmentAdmin)


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'last_name', 'first_name', 'email', 'title', 'department',
        'is_department_head', 'employment_status', 'default_username')
    list_filter = (
        'is_employed', 'department', 'is_department_head',
        'employment_status', 'primary_location')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    readonly_fields = ('guid', 'is_employed')
    search_fields = ('last_name', 'first_name', 'email', 'title', 'bio')
admin.site.register(Member, MemberAdmin)
