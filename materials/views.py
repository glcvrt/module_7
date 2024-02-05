from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from rest_framework.filters import OrderingFilter

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer, CourseLessonSerializer
from users.models import Payments
from users.serializers import PaymentsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class CourseLessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.filter(course__isnull=False)
    serializer_class = CourseLessonSerializer


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_type')
    ordering_fields = ('date',)


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer

