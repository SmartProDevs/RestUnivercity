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
    #
    # path('kafedras/', KafedraView.as_view(), name='kafedras-list'),
    # path('kafedras/<int:pk>', KafedraView.as_view(), name='kafedras-list'),
    #
    # path('subjects/', SubjectView.as_view(), name='subjects-list'),
    # path('subjects/<int:pk>', SubjectView.as_view(), name='subjects-list'),
    #
    # path('teachers/', TeacherView.as_view(), name='teachers-list'),
    # path('teachers/<int:pk>', TeacherView.as_view(), name='teachers-list'),
    #
    # path('faculties/', FacultyView.as_view(), name='faculties-list'),
    # path('faculties/<int:pk>', FacultyView.as_view(), name='faculties-list'),
    #
    # path('groups/', GroupView.as_view(), name='groups-list'),
    # path('groups/<int:pk>', GroupView.as_view(), name='groups-list'),
    #
    # path('students/', StudentView.as_view(), name='students-list'),
    # path('students/<int:pk>', StudentView.as_view(), name='students-list'),

    #####################GENERIC#####################
    path('faculties/create/', FacultyCreateView.as_view(), name="faculty-create"),
    path('faculties/list/', FacultyListView.as_view(), name="faculty-list"),
    path('faculties/<int:pk>/retrieve/', FacultyRetrieveView.as_view(), name="faculty-retrieve"),
    path('faculties/<int:pk>/update/', FacultyUpdateView.as_view(), name="faculty-update"),
    path('faculties/<int:pk>/destroy/', FacultyDestroyView.as_view(), name="faculty-destroy"),

    path('kafedras/create/', KafedraCreateView.as_view(), name="kafedra-create"),
    path('kafedras/list/', KafedraListView.as_view(), name="kafedra-list"),
    path('kafedras/<int:pk>/retrieve/', KafedraRetrieveView.as_view(), name="kafedra-retrieve"),
    path('kafedras/<int:pk>/update/', KafedraUpdateView.as_view(), name="kafedra-update"),
    path('kafedras/<int:pk>/destroy/', KafedraDestroyView.as_view(), name="kafedra-destroy"),

    path('subjects/create/', SubjectCreateView.as_view(), name="subject-create"),
    path('subjects/list/', SubjectListView.as_view(), name="subject-list"),
    path('subjects/<int:pk>/retrieve/', SubjectRetrieveView.as_view(), name="subject-retrieve"),
    path('subjects/<int:pk>/update/', SubjectUpdateView.as_view(), name="subject-update"),
    path('subjects/<int:pk>/destroy/', SubjectDestroyView.as_view(), name="subject-destroy"),

    path('groups/create/', GroupCreateView.as_view(), name="group-create"),
    path('groups/list/', GroupListView.as_view(), name="group-list"),
    path('groups/<int:pk>/retrieve/', GroupRetrieveView.as_view(), name="group-retrieve"),
    path('groups/<int:pk>/update/', GroupUpdateView.as_view(), name="group-update"),
    path('groups/<int:pk>/destroy/', GroupDestroyView.as_view(), name="group-destroy"),

    path('teachers/create/', TeacherCreateView.as_view(), name="teacher-create"),
    path('teachers/list/', TeacherListView.as_view(), name="teacher-list"),
    path('teachers/<int:pk>/retrieve/', TeacherRetrieveView.as_view(), name="teacher-retrieve"),
    path('teachers/<int:pk>/update/', TeacherUpdateView.as_view(), name="teacher-update"),
    path('teachers/<int:pk>/destroy/', TeacherDestroyView.as_view(), name="teacher-destroy"),

    path('students/create/', StudentCreateView.as_view(), name="student-create"),
    path('students/list/', StudentListView.as_view(), name="student-list"),
    path('students/<int:pk>/retrieve/', StudentRetrieveView.as_view(), name="student-retrieve"),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name="student-update"),
    path('students/<int:pk>/destroy/', StudentDestroyView.as_view(), name="student-destroy"),

]