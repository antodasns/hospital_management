# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import lab_tech,Consulting,Tests,Chart
admin.site.register(lab_tech)
admin.site.register(Consulting)
admin.site.register(Tests)
admin.site.register(Chart)

