from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fastlane/index', views.index, name='index'),
    path('fastlane/about-fastlane', views.about, name='about-fastlane'),
    path('fastlane/feedback', views.feedback, name='feedback'),
    path('fastlane/product-services', views.productservices, name='product-services'),
    path('fastlane/fastlane-team', views.fastlaneteam, name='fastlane-team'),
    path('fastlane/help-desk', views.helpdesk, name='help-desk'),
    path('fastlane/report-issue', views.reportissue, name='report-issue'),
    path('fastlane/store', views.store, name='store'),
    path('fastlane/partner', views.partner, name='partner'),
    path('fastlane/sign-in', views.signin, name='sign-in'),
]