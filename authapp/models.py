from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    company_site = models.URLField(verbose_name='Сайт компании', blank=True, null=True)

    def __str__(self):
        return self.user.email
