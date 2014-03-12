from django.contrib import admin
from journal.models import CustomUser, Task
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Task)
