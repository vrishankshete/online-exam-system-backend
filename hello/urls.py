from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('loginAsAdmin', views.loginAsAdmin, name="loginAsAdmin"),
    path('adminpage', views.adminpage, name="adminpage"),
    path('createStudent',views.createStudent, name="createStudent"),
    path('createTeacher', views.createTeacher, name="createTeacher"),
    path('createTeacherAcc', views.createTeacherAcc, name="createTeacherAcc"),
    path('result', views.result, name="result"),
    path('deleteStudent',views.deleteStudent, name="deleteStudent"),
    path('deleteStudentAcc', views.deleteStudentAcc, name="deleteStudentAcc"),
    path('deleteTeacher',views.deleteTeacher, name="deleteTeacher"),
    path('deleteTeacherAcc', views.deleteTeacherAcc, name="deleteTeacherAcc"),

    path('loginAsTeacher', views.loginAsTeacher, name="loginAsTeacher"),
    path('teacherDashboard', views.teacherDashboard, name="teacherDashboard"),
    path('createTest', views.createTest, name="createTest"),

    path('loginAsSudent', views.loginAsStudent, name='loginASStudent'),
    path('studentDashboard', views.StudentDashboard, name='studentDashboard')
]