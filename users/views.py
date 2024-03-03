from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404

from materials.permissions import IsNotStaffUser
from users.models import Payments
from users.serializers import PaymentSerializer, UserSerializer, PaymentCreateSerializer
from users.services import retrieve_session, create_product, create_price, create_session


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_type')
    ordering_fields = ('date',)


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializer

    def perform_create(self, serializer):
        course = serializer.validated_data.get('course')
        if not course:
            raise serializers.ValidationError('Не указан курс.')
        payment = serializer.save()
        payment.user = self.request.user
        if payment.payment_method == '2':
            product = create_product(payment)
            price_id = create_price(payment, product)
            payment.session = create_session(price_id).id
        payment.save()


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        if obj.session:
            session = retrieve_session(obj.session)
            if session.payment_status == 'paid' and session.status == 'complete':
                obj.is_successful = True
                obj.save()
        self.check_object_permissions(self.request, obj)
        return obj


class PaymentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsNotStaffUser]


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
