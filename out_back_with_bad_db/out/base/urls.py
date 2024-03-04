from django.urls import path
from base.old_db.views import FacultyList, PracticesList

urlpatterns = [
    path("faculty/", FacultyList.as_view(),  name="faculty_list"),
    path("practice/", PracticesList.as_view(),  name="practice_list")
]
