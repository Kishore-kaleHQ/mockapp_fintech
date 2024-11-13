# core/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum
from .models import Portfolio, Investment, Insurance
from .serializers import (
    PortfolioSerializer,
    InvestmentSerializer,
    InsuranceSerializer
)

class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Portfolio.objects.none()
        return Portfolio.objects.filter(user=self.request.user)

    @action(detail=True, methods=['get'])
    def summary(self, request, pk=None):
        portfolio = self.get_object()
        investments = portfolio.investments.all()
        
        summary = {
            'total_invested': investments.aggregate(Sum('amount'))['amount__sum'] or 0,
            'current_value': investments.aggregate(Sum('current_value'))['current_value__sum'] or 0,
            'by_type': {}
        }
        
        for inv_type, _ in Investment.INVESTMENT_TYPES:
            type_investments = investments.filter(investment_type=inv_type)
            summary['by_type'][inv_type] = {
                'invested': type_investments.aggregate(Sum('amount'))['amount__sum'] or 0,
                'current_value': type_investments.aggregate(Sum('current_value'))['current_value__sum'] or 0
            }
            
        return Response(summary)

class InvestmentViewSet(viewsets.ModelViewSet):
    serializer_class = InvestmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Investment.objects.none()
        return Investment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        portfolio, _ = Portfolio.objects.get_or_create(user=self.request.user)
        serializer.save(user=self.request.user, portfolio=portfolio)

class InsuranceViewSet(viewsets.ModelViewSet):
    serializer_class = InsuranceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Insurance.objects.none()
        return Insurance.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def upcoming_renewals(self, request):
        from django.utils import timezone
        from datetime import timedelta
        
        thirty_days_later = timezone.now().date() + timedelta(days=30)
        upcoming = self.get_queryset().filter(
            renewal_date__lte=thirty_days_later,
            renewal_date__gte=timezone.now().date(),
            is_active=True
        )
        
        serializer = self.get_serializer(upcoming, many=True)
        return Response(serializer.data)

class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if getattr(self, 'swagger_fake_view', False):
            return Response({
                'message': 'Dashboard data will be available here'
            })

        portfolio, _ = Portfolio.objects.get_or_create(user=request.user)
        investments = Investment.objects.filter(user=request.user)
        insurances = Insurance.objects.filter(user=request.user, is_active=True)
        
        data = {
            'portfolio_summary': {
                'total_invested': investments.aggregate(Sum('amount'))['amount__sum'] or 0,
                'current_value': investments.aggregate(Sum('current_value'))['current_value__sum'] or 0,
            },
            'investment_summary': {
                'total_investments': investments.count(),
                'types': {}
            },
            'insurance_summary': {
                'total_policies': insurances.count(),
                'total_premium': insurances.aggregate(Sum('premium'))['premium__sum'] or 0,
                'total_coverage': insurances.aggregate(Sum('coverage_amount'))['coverage_amount__sum'] or 0
            }
        }
        
        for inv_type, _ in Investment.INVESTMENT_TYPES:
            type_investments = investments.filter(investment_type=inv_type)
            data['investment_summary']['types'][inv_type] = {
                'count': type_investments.count(),
                'invested': type_investments.aggregate(Sum('amount'))['amount__sum'] or 0,
                'current_value': type_investments.aggregate(Sum('current_value'))['current_value__sum'] or 0
            }
        
        return Response(data)
