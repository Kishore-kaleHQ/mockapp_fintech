# core/admin.py
from django.contrib import admin
from .models import Portfolio, Investment, Insurance

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_value', 'last_valuation_date')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'investment_type', 'amount', 'current_value', 'get_return_display')
    list_filter = ('investment_type', 'purchase_date')
    search_fields = ('user__username', 'name')
    readonly_fields = ('created_at', 'updated_at')

    def get_return_display(self, obj):
        return f"{obj.get_return():.2f}%"
    get_return_display.short_description = 'Return %'

@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'user', 'policy_type', 'provider', 'premium', 'is_active')
    list_filter = ('policy_type', 'is_active', 'provider')
    search_fields = ('user__username', 'policy_number', 'provider')
    readonly_fields = ('created_at', 'updated_at')
    
    list_per_page = 20
