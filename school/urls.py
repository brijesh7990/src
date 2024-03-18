from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path("dashboard/", login_required(views.DashboardView.as_view()), name="dashboard"),
    path("students/", login_required(views.StudentView.as_view()), name="students"),
    path("parents/", login_required(views.ParentView.as_view()), name="parents"),
    path("teachers/", login_required(views.TeacherView.as_view()), name="teachers"),
    path("addstudent/", login_required(views.AddStudentView.as_view()), name="addstudent"),
    path("addparent/", login_required(views.AddParentView.as_view()), name="addparent"),
    path("addteacher/", login_required(views.AddTeacherView.as_view()), name="addteacher"),


    path("studentajax/", login_required(views.StudentAjaxView.as_view()), name="studentajax"),
    path("parentajax/", login_required(views.ParentAjaxView.as_view()), name="parentajax"),
    path("teacherajax/", login_required(views.TeacherAjaxView.as_view()), name="teacherajax"),

]
