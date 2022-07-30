from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Partner, Feedback, Team, OjtTeam
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm


def index(request):
    partner_logo=Partner.objects.all
    feedback_profile=Feedback.objects.all
    return render(request,"fastlane/index.html",{"partner_logo":partner_logo,"feedback_profile":feedback_profile})

def about(request):
    partner_logo=Partner.objects.all
    feedback_profile=Feedback.objects.all
    return render(request,"fastlane/about-fastlane.html",{"partner_logo":partner_logo,"feedback_profile":feedback_profile})

def feedback(request):
    feedback_profile=Feedback.objects.all
    return render(request,"fastlane/feedback.html",{"feedback_profile":feedback_profile})

def productservices(request):
    return render(request,"fastlane/product-services.html")

def fastlaneteam(request):
    team_profile=Team.objects.all
    ojt_profile=OjtTeam.objects.all
    return render(request,"fastlane/fastlane-team.html",{"team_profile":team_profile, "ojt_profile":ojt_profile})

def helpdesk(request):
    return render(request,"fastlane/help-desk.html")

def reportissue(request):
    return render(request,"fastlane/report-issue.html")

def store(request):
    return render(request,"fastlane/store.html")

def partner(request):
    partner_logo=Partner.objects.all
    if request.method == 'POST':
            form = ContactForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']

                html = render_to_string('fastlane/infocontact.html', {
                    'name': name,
                    'email': email,
                    'subject': subject,
                    'message': message
                })

                send_mail(subject, message , email, ['fastlanetest123@gmail.com'], html_message=html)

                return redirect('index')
    else:
            form = ContactForm()
    return render(request,"fastlane/partner.html",{"partner_logo":partner_logo,'form': form})

def signin(request):
    return render(request,"fastlane/sign-in.html")