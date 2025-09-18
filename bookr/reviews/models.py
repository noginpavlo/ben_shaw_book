from django.db import models


class Publisher(models.Model):
    """A company that publishes books."""

    name = models.CharField(max_length=50, help_text="The name of the publisher.")
    website = models.URLField(help_text="The publisher's website.")
    email = models.EmailField(help_text="The publisher's email address.")


class Book(models.Model):
    """A published book"""

    title = models.CharField(max_length=70, help_text="The title of the book.")
    publication_date = models.DateField(verbose_name="Date the book was published.")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book.")


class Contributor(models.Model):
    """A contributor to a Book, e.g. author, editor, co-author."""

    first_name = models.CharField(max_length=50, help_text="The contributor's first name.")
    last_name = models.CharField(max_length=50, help_text="The contributor's last name.")
    email = models.EmailField(help_text="The contact email for the contributor.")
