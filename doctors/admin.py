# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Doctor,Doctor_timing
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Doctor_timing)