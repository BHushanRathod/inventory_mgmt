from uuid import uuid4
from django.db import models


def generate_unique():
    return uuid4().hex[:6].lower()


# Create your models here.
class InvertoryStack(models.Model):
    id = models.CharField(default=generate_unique, primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    is_active = models.BooleanField(default=1)
    readonly_fields = ["id"]

    def __str__(self):
        return self.name


class Purchase(models.Model):
    item_id = models.ForeignKey(InvertoryStack, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
