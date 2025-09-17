from django.db import models


class Publisher(models.Model):
    """A company that publishes books."""

    name = models.CharField(max_length=150, help_text="The name of the publisher.")
    website = models.URLField(help_text="The publisher's website.")
    email = models.EmailField(help_text="The publisher's email address.")
