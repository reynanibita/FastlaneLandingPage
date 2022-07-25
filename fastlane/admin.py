from django.contrib import admin
from .models import Partner, Feedback, Team, OjtTeam
# Register your models here.
admin.site.register(Partner)
admin.site.register(Feedback)
admin.site.register(Team)
admin.site.register(OjtTeam)