from django.db import models
from account.models import User

# Create your models here.
class Charge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    number = models.CharField(max_length=50, null=True, blank=False)
    exp_month = models.CharField(max_length=50, null=True, blank=False)
    exp_year = models.CharField(max_length=50, null=True, blank=False)
    cvc = models.CharField(max_length=50, null=True, blank=False)

    stripe_charge_id = models.CharField(max_length=50)
    currency = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.pk}.{self.user}"
    

