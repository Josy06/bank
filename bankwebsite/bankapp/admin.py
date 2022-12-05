from django.contrib import admin
from .models import Team
from .models import Person,Districts,Branch

# Register your models here.

admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Districts)
admin.site.register(Branch)