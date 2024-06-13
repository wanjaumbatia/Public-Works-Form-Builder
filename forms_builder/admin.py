from django.contrib import admin
from forms_builder.models import Form, Section, Field, FieldChoice

# Register your models here.
admin.site.register(Form)
admin.site.register(Section)
admin.site.register(Field)
admin.site.register(FieldChoice)