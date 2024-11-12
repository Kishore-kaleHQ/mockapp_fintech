# core/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseTimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Portfolio(BaseTimestampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='portfolio')
    total_value = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    last_valuation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Portfolio"

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

class Investment(BaseTimestampModel):
    INVESTMENT_TYPES = [
        ('STOCKS', 'Stocks'),
        ('BONDS', 'Bonds'),
        ('MUTUAL_FUNDS', 'Mutual Funds'),
        ('ETF', 'ETF'),
        ('FD', 'Fixed Deposit'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investments')
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='investments')
    investment_type = models.CharField(max_length=20, choices=INVESTMENT_TYPES)  # Fixed here
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    purchase_date = models.DateField()
    current_value = models.DecimalField(max_digits=15, decimal_places=2)
    units = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    notes = models.TextField(blank=True, null=True)

    def get_return(self):
        return ((self.current_value - self.amount) / self.amount * 100)

    def __str__(self):
        return f"{self.name} ({self.investment_type})"

    class Meta:
        verbose_name = 'Investment'
        verbose_name_plural = 'Investments'

class Insurance(BaseTimestampModel):
    POLICY_TYPES = [
        ('LIFE', 'Life Insurance'),
        ('HEALTH', 'Health Insurance'),
        ('TERM', 'Term Insurance'),
        ('VEHICLE', 'Vehicle Insurance'),
        ('PROPERTY', 'Property Insurance'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='insurances')
    policy_type = models.CharField(max_length=20, choices=POLICY_TYPES)
    policy_number = models.CharField(max_length=50, unique=True)
    provider = models.CharField(max_length=255)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_amount = models.DecimalField(max_digits=15, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    renewal_date = models.DateField()

    def __str__(self):
        return f"{self.get_policy_type_display()} - {self.policy_number}"

    class Meta:
        verbose_name = 'Insurance'
        verbose_name_plural = 'Insurance Policies'
