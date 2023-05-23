from django.db import models
from django.utils import timezone


class Item_GS(models.Model):
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # title = models.CharField(max_length=100)
    # content = models.TextField()
    item_idx = models.CharField(max_length=100, primary_key=true)
    name = models.CharField(max_length=40)
    price = models.IntegerField(max_length=7)
    img = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expired_at = models.DateTimeField(blank=True, null=True)

    # def publish(self):
    #     self.published_at = timezone.now()
    #     self.save()

    def __str__(self):
        return self.name
