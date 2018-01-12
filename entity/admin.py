from django.contrib import admin
from models import Location, Tag, Card, UserProfile, Department, PublicNotice, PersonalNotice
# Register your models here.

admin.site.register(Location)
admin.site.register(Tag)
admin.site.register(Card)
admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(PublicNotice)
admin.site.register(PersonalNotice)