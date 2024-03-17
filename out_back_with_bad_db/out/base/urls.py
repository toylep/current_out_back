from django.urls import path

from base.views import (
    DocLinkCreateView,
    PracticesList,
    PracticeCreateView,
    CompanyListView,
    SpecilityCreateView,
    CompanySingleView,
    CompanyCreateView,
    ThemeCreateView,
    )
urlpatterns = [
   
    path("practice/", PracticesList.as_view(), name="practice_list"),
    path("practice/add", PracticeCreateView.as_view(), name="practice_add"),
    path("company/", CompanyListView.as_view(), name="company_list"),
    path("company/", CompanyCreateView.as_view(), name="company_add"),
    path("company/<int:pk>", CompanySingleView.as_view(), name="company_list"),
    path("theme/add", ThemeCreateView.as_view(), name="company_add"),
    path("speciality/add", SpecilityCreateView.as_view(), name="speciality_add"),
    path("diclinks/add", DocLinkCreateView.as_view(), name="doclinks-add")
]
