from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='courses/thumbnails/', null=True, blank=True)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    author = models.CharField(max_length=120, default='Admin')
    pdf = models.FileField(upload_to='courses/pdfs/', null=True, blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    video_url = models.URLField(blank=True)
    free_preview = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=200, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=200, blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
