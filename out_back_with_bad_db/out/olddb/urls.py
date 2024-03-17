from django.urls import path


from olddb.views import (
    FacultyList,
    FacultyCreateView,
    FacultySingleView,
)
urlpatterns = [
    path("faculty/", FacultyList.as_view(), name="faculty_list"),
    path("faculty/", FacultyCreateView.as_view(), name="faculty_add"),
    path("faculty/<int:pk>", FacultySingleView.as_view(), name="faculty_single"),
]
