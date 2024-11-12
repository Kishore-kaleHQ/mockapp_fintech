# core/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Portfolio, Investment, Insurance

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = fields

class InvestmentSerializer(serializers.ModelSerializer):
    return_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Investment
        fields = (
            'id', 'investment_type', 'name', 'amount', 'purchase_date',
            'current_value', 'units', 'notes', 'return_percentage'
        )
        read_only_fields = ('user', 'portfolio')

    def get_return_percentage(self, obj):
        return obj.get_return()

class InsuranceSerializer(serializers.ModelSerializer):
    days_to_renewal = serializers.SerializerMethodField()
    policy_type_display = serializers.CharField(source='get_policy_type_display', read_only=True)

    class Meta:
        model = Insurance
        fields = (
            'id', 'policy_type', 'policy_type_display', 'policy_number',
            'provider', 'premium', 'coverage_amount', 'start_date',
            'end_date', 'is_active', 'renewal_date', 'days_to_renewal'
        )
        read_only_fields = ('user',)

    def get_days_to_renewal(self, obj):
        from django.utils import timezone
        delta = obj.renewal_date - timezone.now().date()
        return delta.days

class PortfolioSerializer(serializers.ModelSerializer):
    investments = InvestmentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Portfolio
        fields = ('id', 'user', 'total_value', 'last_valuation_date', 'investments')
        read_only_fields = ('user',)
