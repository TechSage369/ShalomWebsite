from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path(
        '',
        views.homepage_view,
        name="homepage"
        ),

    path(
        'about-us',
        views.about_us_view,
        name="about_us"
        ),

    path(
        'admission-form',
        views.admission_form,
        name="admission-form"
        ),

    path(
        'admission',
        views.admission_view,
        name="admission"
        ),

    path(
        'annual-planner',
        views.annual_planner_view,
        name='annual_planner'
        ),

    path(
        'principle-letter',
        views.principle_letter,
        name='principle_letter'
        ),

    path(
        'rules-and-regulations',
        views.rules_and_regulations_view,
        name="rules_and_regulations"
        ),

    path(
        'vision-and-mission',
        views.vision_and_mission_view,
        name="vision_and_mission"
        ),

    path(
        'administration',
        views.administration_view,
        name="administration"
        ),


    #  galleries paths
    path(
        'gallery',
        views.gallery_view,
        name='gallery'
    ),
    path(
        'gallery/<str:slug>',
        views.gallery_details_view,
        name="gallery_detail"
        ),
    path(
        'teachers-day',
        views.gallery_teachers_day_view,
        name="gallery_teachers_day"
    ),
    path(
        'childrens-day',
        views.gallery_childrens_day_view,
        name='gallery_childrens_day'
        ),
    path(
        'investiture-ceremony',
        views.gallery_investiture_ceremony_view,
        name="gallery_investiture_ceremony"
        ),
    path(
        'environment-day',
        views.gallery_environment_day_view,
        name='gallery_environment_day'
        ),
    path(
        'christmas-day',
        views.gallery_christmas_day_view,
        name="gallery_christmas_day"
        ),
    path(
        'sports-day',
        views.gallery_sports_day_view,
        name="gallery_sports_day"
        ),
    path(
        'independence-day',
        views.gallery_independence_day_view,
        name='gallery_independence_day'
        ),
    path(
        'school-activities',
        views.gallery_school_activities_view,
        name="gallery_school_activities"
            )
]
