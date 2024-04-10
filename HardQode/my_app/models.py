from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from random import shuffle


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    min_users = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()

    def __dir__(self):
        return self.name


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    video_link = models.URLField()

    def __dir__(self):
        return self.name


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    students = models.ManyToManyField(User)
    name = models.CharField(max_length=255)

    def __dir__(self):
        return self.name

    def clean(self):
        min_users = self.product.min_users
        max_users = self.product.max_users
        if self.students.count() < min_users or self.students.count() > max_users:
            raise ValidationError("Invalid number of students for this group.")

    def distribute_users(self):
        if self.product.start_date > timezone.now():
            all_users = self.students.all()
            shuffle(all_users)

            groups = [list(all_users[i:i + self.product.max_users_per_group]) for i in
                      range(0, len(all_users), self.product.max_users_per_group)]

            remainder = len(all_users) % self.product.max_users_per_group

            for i in range(remainder):
                groups[i].append(all_users.pop())

            for i in range(self.product.max_users_per_group - remainder):
                groups[i % remainder].append(all_users.pop())

            for i, group in enumerate(groups):
                self.students.set(group)
