from django.contrib import admin
from profiles.models import Profile
from lettings.models import Letting
from lettings.models import Address

admin.site.register(Address)
admin.site.register(Letting)
admin.site.register(Profile)
