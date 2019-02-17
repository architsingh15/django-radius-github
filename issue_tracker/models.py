from django.db import models


class Registry(models.Model):
    """
    The DB schema for the registry model to store the issues data to be shown on Issue Registry page
    """
    class Meta:
        verbose_name_plural = "Registry"

    def __str__(self):
        return self.repository_name

    repository_name = models.CharField(max_length=100, blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False)
    total = models.PositiveIntegerField(blank=False, null=False)
    last_24_hours = models.PositiveIntegerField(blank=False, null=False)
    between_1_and_7_days = models.PositiveIntegerField(blank=False, null=False)
    more_than_7_days = models.PositiveIntegerField(blank=False, null=False)
