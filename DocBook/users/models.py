from django.contrib.auth.models import AbstractUser
from django.db import models
from DocBook.conf import BRANCH_CHOICES


class User(AbstractUser):
    branch = models.CharField(
        verbose_name='Отделение',
        max_length=max(len(branch) for branch, show in BRANCH_CHOICES),
        choices=BRANCH_CHOICES
    )

    @property
    def get_branch(self):
        return self.branch
