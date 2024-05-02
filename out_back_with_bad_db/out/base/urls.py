from django.urls import path

from base.views import (
    DocLinkCreateView,
    PracticesList,
    PracticeCreateView,
    SpecilityCreateView,
    ThemeCreateView,
    SpecialitySingleView,
    SpecialityList
    )
urlpatterns = [
   
    path("practice/", PracticesList.as_view(), name="practice_list"),
    path("practice/add", PracticeCreateView.as_view(), name="practice_add"),
    path("theme/add", ThemeCreateView.as_view(), name="company_add"),
    path("speciality/add", SpecilityCreateView.as_view(), name="speciality_add"),
    path("speciality/", SpecialityList.as_view(), name="speciality_list"),
    path("speciality/<int:pk>", SpecialitySingleView.as_view(), name="speciality_single"),
    path("doclinks/add", DocLinkCreateView.as_view(), name="doclinks-add")
]
