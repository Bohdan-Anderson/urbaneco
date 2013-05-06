from django.contrib import admin
from urbaneco.models import Person, Event, Theme, Membership

admin.site.register(Event)
admin.site.register(Person)
admin.site.register(Theme)
admin.site.register(Membership)
