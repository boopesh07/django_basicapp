from django.contrib import admin
from myfirst_app.models import Topic,Webpage,AccessRecord,UserProf

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(UserProf)
# Register your models here.
