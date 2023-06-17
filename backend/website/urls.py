from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.homepage_view, name="homepage"),
    path('about-us', views.about_us_view, name="about_us"),
    path('admission-form', views.admission_form, name="admission-form"),
    path('admission', views.admission_view, name="admission"),
    path('annual-planner', views.annual_planner_view, name='annual_planner'),
    path('gallery', views.gallery_view, name='gallery'),
    path('principle-letter', views.principle_letter, name='principle_letter'),
    path('rules-and-regulations', views.rules_and_regulations_view, name="rules_and_regulations"),
    path('vision-and-mission', views.vision_and_mission_view, name="vision_and_mission"),
    path('administration', views.administration_view, name="administration")
]
