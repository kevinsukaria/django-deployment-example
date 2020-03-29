from django.contrib import admin
from first_app.models import Webpage, Topic, Accessrecord
# Register your models here.

admin.site.register(Accessrecord)
admin.site.register(Topic)
admin.site.register(Webpage)