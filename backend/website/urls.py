from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.homepage_view, name="homepage"),
    path('about-us', views.about_us_view, name="about_us"),
    path('admission-form', views.admission_form, name="admission-form"),
    path('admission', views.admission_view, name="admission"),
    path('fee-structure', views.fee_structure_view, name='fee_structure'),
    path('gallery', views.gallery_view, name='gallery')
]
