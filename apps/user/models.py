from django.db import models


class Permissions(models.Model):
    class Meta:
        app_label = 'user'
        managed = False  # No database management for this model
        # Add here all the application permissions
        permissions = (
            ('admin', 'Admin'),
            ('read_only', 'Read Only'),
        )
