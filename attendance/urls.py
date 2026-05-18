from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),
     
    path(
        'list/',
        views.attendance_list,
        name='attendance_list'
    ),


     path(
        '',
        views.attendance_list,
        name='attendance_list'
    ),

    path(
        'records/',
        views.attendance_records,
        name='attendance_records'
    ),

    path(
        'view/<int:id>/',
        views.view_attendance,
        name='view_attendance'
    ),

    path(
        'edit/<int:id>/',
        views.edit_attendance,
        name='edit_attendance'
    ),

    path(
        'delete/<int:id>/',
        views.delete_attendance,
        name='delete_attendance'
    ),





    #API URLS 

      path(

        'api/attendance/',views.

        AttendanceListCreateAPI.as_view(),

        name='attendance_api'

    ),

    path(

        'api/attendance/<int:pk>/',views.

        AttendanceRetrieveUpdateDeleteAPI.as_view(),

        name='attendance_detail_api'

    ),

]