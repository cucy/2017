from django.db import models

# Create your models here.
#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/6/30 14:11
# Author: zhourudong

from django.urls import reverse
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})