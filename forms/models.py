from django.db import models

from django.contrib.auth.models import User
from forms_builder.models import Form

class Submission(models.Model):    
    form = models.ForeignKey(Form, related_name='submissions', on_delete=models.PROTECT)
    submission_date = models.DateTimeField("Submission Date", auto_now=True)    
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    data = models.JSONField('Data')
    
    class Meta:
        verbose_name = "submission"
        verbose_name_plural = "submissions"

