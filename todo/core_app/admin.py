from django.contrib import admin
from core_app.models import CheckList,CheckListItem
# Register your models here.

admin.site.register(CheckList)
admin.site.register(CheckListItem)