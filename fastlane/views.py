from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Partner, Feedback, Team, OjtTeam


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
        
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        name = request.POST.get('name')        
        email = request.POST.get('email')
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        return render(request, "fastlane/email_sent.html", {'email': email})
        
    partner_logo=Partner.objects.all
    return render(request,"fastlane/partner.html",{"partner_logo":partner_logo})

def signin(request):
    return render(request,"fastlane/sign-in.html")