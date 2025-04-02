from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class HeritageSite(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='heritage_sites/', null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    site = models.ForeignKey(HeritageSite, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

    def __str__(self):
        return f"{self.name}'s Review on {self.site.name} ({self.rating}/5)"
