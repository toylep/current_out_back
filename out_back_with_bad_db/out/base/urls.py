from django.urls import path

from base.views import (
    DocLinkCreateView,
    PracticesList,
    PracticeCreateView,
    SpecilityCreateView,
    ThemeCreateView,
    )
urlpatterns = [
   
    path("practice/", PracticesList.as_view(), name="practice_list"),
    path("practice/add", PracticeCreateView.as_view(), name="practice_add"),
   
    path("theme/add", ThemeCreateView.as_view(), name="company_add"),
    path("speciality/add", SpecilityCreateView.as_view(), name="speciality_add"),
    path("doclinks/add", DocLinkCreateView.as_view(), name="doclinks-add")
]
