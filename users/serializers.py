from rest_framework import serializers

from users.models import Payments, User


class PaymentSerializer(serializers.ModelSerializer):
    payment_method = serializers.SerializerMethodField()

    def get_payment_method(self, obj):
        if obj.payment_method == '1':
            return "Наличные"
        elif obj.payment_method == '2':
            return "Безнал"

    class Meta:
        model = Payments
        fields = ('id', 'user', 'course', 'payment_date', 'payment_method', 'session', 'is_successful')


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ('course', 'payment_method')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



