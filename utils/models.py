from django.db import models


class StoreModel(models.Model):
    """
    Basic model that gives another parameters to any other model.
    """
    created_at = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    updated_at = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:

        abstract = True
        get_latest_by = 'created_at'
        ordering = ['-created_at', '-updated_at']
