"""Sermons app models"""
from django.db import models

class Serie(models.Model):
    """Serie model to group sermons"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)


class Sermon(models.Model):
    """Each video to show"""
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    video_url = models.URLField(max_length=200)
    image_url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
