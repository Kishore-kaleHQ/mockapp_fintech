# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PortfolioViewSet,
    InvestmentViewSet,
    InsuranceViewSet,
    DashboardView
)

router = DefaultRouter()
router.register(r'portfolios', PortfolioViewSet, basename='portfolio')
router.register(r'investments', InvestmentViewSet, basename='investment')
router.register(r'insurance', InsuranceViewSet, basename='insurance')

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
