from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Title'
    )
    description = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='description'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='updated_at'
    )

    class Meta:
        ordering = ['-updated_at', '-created_at']
