from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Public Works OFMS'
        sender_email = 'no-reply@publicworks.go.ke'  # Change this to your sender email
        recipient_email = instance.email
        token = default_token_generator.make_token(instance)
        User = get_user_model()
        uid = instance.id
        reset_url = reverse('password_reset_confirm', args=[uid, token])
        password_set_url = 'http://127.0.0.1:8000' + reset_url  # Change this to your actual domain
        html_message = render_to_string('emails/welcome_email.html', {'user': instance, 'link': password_set_url})  
        print(reset_url)      
        #send_mail(subject, None, sender_email, [recipient_email], html_message=html_message)
