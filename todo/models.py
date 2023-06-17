from typing import Any, Dict, Tuple
from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Does(models.Model):
    title=models.CharField(max_length=60)
    text=models.TextField()
    active=models.BooleanField(default=True)
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default=get_user_model())
    def __str__(self) -> str:
        return f"Owner: {self.user.get_username()} {self.title}"
    def get_absolute_url(self):
        return reverse("do_detail", kwargs={"id": self.id})

    
    