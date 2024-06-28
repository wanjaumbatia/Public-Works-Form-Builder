from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from forms_builder.models import Form
from forms.models import Submission

@login_required(login_url='/login')
def homepage(request):
    users_count = User.objects.count()
    published_count = Form.objects.filter(status='published').count()
    draft_count = Form.objects.filter(status='draft').count()
    total_submissions = Submission.objects.count()
    return render(request,'index.html', {'users_count': users_count, 'published_count': published_count, 'draft_count': draft_count, 'total_submissions': total_submissions})