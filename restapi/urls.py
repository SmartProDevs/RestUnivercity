from django.urls import path, include
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
#
# router.register(r"kafedras", KafedraViewSet)
# router.register(r"subjects", SubjectViewSet)
# router.register(r"teachers", TeacherViewSet)
# router.register(r"faculties", FacultyViewSet)
# router.register(r"groups", GroupViewSet)
# router.register(r"students", StudentViewSet)

urlpatterns = [
    # path('', include(router.urls))
    path('kafedras/', KafedraView.as_view(), name='kafedras-list'),
    path('kafedras/<int:pk>', KafedraView.as_view(), name='kafedras-list'),

    path('subjects/', SubjectView.as_view(), name='subjects-list'),
    path('subjects/<int:pk>', SubjectView.as_view(), name='subjects-list'),

    path('teachers/', TeacherView.as_view(), name='teachers-list'),
    path('teachers/<int:pk>', TeacherView.as_view(), name='teachers-list'),

    path('faculties/', FacultyView.as_view(), name='faculties-list'),
    path('faculties/<int:pk>', FacultyView.as_view(), name='faculties-list'),

    path('groups/', GroupView.as_view(), name='groups-list'),
    path('groups/<int:pk>', GroupView.as_view(), name='groups-list'),

    path('students/', StudentView.as_view(), name='students-list'),
    path('students/<int:pk>', StudentView.as_view(), name='students-list'),

]