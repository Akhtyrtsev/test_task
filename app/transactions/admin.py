from django.contrib import admin


from transactions.models import User, Operation
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    pass