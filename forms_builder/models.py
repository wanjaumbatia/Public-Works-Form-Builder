from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Form(models.Model):    
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("maintainance", "Pulled Down")
    ]
    
    name=models.CharField(max_length=255)
    description = models.CharField("Description", max_length=255, blank=True, null=True)
    status = models.CharField("Status", choices=STATUS_CHOICES, max_length=50, default='draft')
    created_on = models.DateTimeField("created On", auto_now=True)
    published_on = models.DateTimeField("Published On", auto_now=False, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='form_create_user', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Section(models.Model):
    name = models.CharField(max_length=255)
    form = models.ForeignKey(Form, related_name="sections", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
   
class Field(models.Model):
    FIELD_TYPE_CHOICES =[
        ("text", "Text"),
        ("number", "Number"),
        ("email", "Email"),
        ("phone", "Phone"),
        ("radio", "Radio"),
        ("checkbox", "Checkbox"),
        ("select", "Select"),
        ("file", "File"),
    ]
    
    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=50, choices=FIELD_TYPE_CHOICES)
    order = models.IntegerField(default=0)
    section = models.ForeignKey(Section, related_name="form_fields", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.label
    
    class Meta:
        ordering = ['order']
    
class FieldChoice(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="choices")
    order = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.choice_text