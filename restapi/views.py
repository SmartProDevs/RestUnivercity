from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView

# class KafedraViewSet(ModelViewSet):
#     queryset = Kafedra.objects.all()
#     serializer_class = KafedraSerializer
#
# class SubjectViewSet(ModelViewSet):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer
#
# class TeacherViewSet(ModelViewSet):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
# class FacultyViewSet(ModelViewSet):
#     queryset = Faculty.objects.all()
#     serializer_class = FacultySerializer
#
# class GroupViewSet(ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
# class StudentViewSet(ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class KafedraView(APIView):

    def get_object(self, pk):
        try:
            model = Kafedra.objects.get(pk=pk)
        except Exception:
            raise NotFound("Author not found -----------")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            kafedra = self.get_object(kwargs.get("pk"))
            serializer = KafedraSerializer(kafedra, many=False)
            return Response(serializer.data)
        else:
            kafedras = Kafedra.objects.all()
            serializer = KafedraSerializer(kafedras, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = KafedraSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        kafedra = self.get_object(kwargs.get("pk"))
        serializer = KafedraSerializer(data=request.data, instance=kafedra)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        kafedra = self.get_object(kwargs.get("pk"))
        kafedra.delete()
        return Response({"state": "deleted"})

class SubjectView(APIView):

    def get_object(self, pk):
        try:
            model = Subject.objects.get(pk=pk)
        except Exception:
            return NotFound("Ma'lumot mavjud emas")
        return model

    def get(self, *args, **kwargs):
        if kwargs.get("pk"):
            subject = self.get_object(kwargs.get("pk"))
            serializer = SubjectSerializer(subject, many=False)
            return Response(serializer.data)
        else:
            subject = Subject.objects.all()
            serializer = SubjectSerializer(subject, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self,request, *args, **kwargs):
        subject = self.get_object(kwargs.get("pk"))
        serializer = SubjectSerializer(data = request.data, instance=subject )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        subject = self.get_object(kwargs.get("pk"))
        subject.delete()
        return Response({'state': 'deleted'})

class TeacherView(APIView):

    def get_object(self, pk):
        try:
            model = Teacher.objects.get(pk=pk)
        except Exception:
            return NotFound("Ma'lumot mavjud emas")
        return model

    def get(self, *args, **kwargs):
        if kwargs.get("pk"):
            model = self.get_object(kwargs.get("pk"))
            serializer = TeacherSerializer(model, many=False)
            return Response(serializer.data)
        else:
            model = Teacher.objects.all()
            serializer = TeacherSerializer(model, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        serializer = TeacherSerializer(data=request.data, instance=model)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        model.delete()
        return Response({'state': 'deleted'})

class FacultyView(APIView):

    def get_object(self, pk):
        try:
            model = Faculty.objects.get(pk=pk)
        except Exception:
            return NotFound("Ma'lumot mavjud emas")
        return model

    def get(self, *args, **kwargs):
        if kwargs.get("pk"):
            model = self.get_object(kwargs.get("pk"))
            serializer = FacultySerializer(model, many=False)
            return Response(serializer.data)
        else:
            model = Faculty.objects.all()
            serializer = FacultySerializer(model, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = FacultySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        serializer = FacultySerializer(data=request.data, instance=model)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        model.delete()
        return Response({'state': 'deleted'})

class GroupView(APIView):

    def get_object(self, pk):
        try:
            model = Group.objects.get(pk=pk)
        except Exception:
            return NotFound('mavjud emas')
        return model

    def get(self,request,*args, **kwargs):

        if kwargs.get("pk"):
            model = self.get_object(kwargs.get("pk"))
            serializer = GroupSerializer(model, many=False)
            return Response(serializer.data)

        else:
            model = Group.objects.all()
            serializer = GroupSerializer(model, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        serializer = GroupSerializer(data=request.data, instance=model)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def delete(self,request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        model.delete()
        return Response({"state": "deleted"})

class StudentView(APIView):

    def get_object(self, pk):
        try:
            model = Student.objects.get(pk=pk)
        except Exception:
            return NotFound('mavjud emas')
        return model

    def get(self, request, *args, **kwargs):

        if kwargs.get("pk"):
            model = self.get_object(kwargs.get("pk"))
            serializer = StudentSerializer(instance=model, many=False)
            return Response(serializer.data)

        else:
            model = Student.objects.all()
            serializer = StudentSerializer(instance=model, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        serializer = StudentSerializer(data=request.data, instance=model)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        model.delete()
        return Response({"state": "deleted"})

############generic views#######################
class KafedraCreateView(CreateAPIView):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer
    
class KafedraUpdateView(UpdateAPIView):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer
    
class KafedraRetrieveView(RetrieveAPIView):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer

class KafedraDestroyView(DestroyAPIView):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer 

class KafedraListView(ListAPIView):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer

###################Faculty########################
class FacultyCreateView(CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyUpdateView(UpdateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyRetrieveView(RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyDestroyView(DestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyListView(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer 

##############Subject############# 
class SubjectCreateView(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectUpdateView(UpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectRetrieveView(RetrieveAPIView):
    queryset = Kafedra.objects.all()
    serializer_class = SubjectSerializer


class SubjectDestroyView(DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectListView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer 

###########GROUP############## 
class GroupCreateView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupUpdateView(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupRetrieveView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDestroyView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer 

########TEACHER####################
class TeacherCreateView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherUpdateView(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherRetrieveView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDestroyView(DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer 

###########STUDENT##################
class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroyView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
