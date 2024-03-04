from django.urls import path
from base.old_db.views import (
    FacultyList,
    PracticesList,
    PracticeCreateView,
    CompanyListView,
    ThemeCreateView,
    SpecilityCreateView
)

urlpatterns = [
    path("faculty/", FacultyList.as_view(), name="faculty_list"),
    path("practice/", PracticesList.as_view(), name="practice_list"),
    path("practice/add", PracticeCreateView.as_view(), name="practice_add"),
    path("company/", CompanyListView.as_view(), name="company_list"),
    path("theme/add", ThemeCreateView.as_view(), name="company_add"),
    path("speciality/add", SpecilityCreateView.as_view(), name="speciality_add")

]
