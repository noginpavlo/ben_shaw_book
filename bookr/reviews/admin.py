from django.contrib import admin
from django.contrib.admin import AdminSite
from reviews.models import Book, BookContributor, Contributor, Publisher, Review


class BookrAdminSite(AdminSite):
    title_header = "Bookr Admin"
    site_header = "Bookr administration"
    index_title = "Bookr site admin"


admin_site = BookrAdminSite(name="bookr")


# Register your models here
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)
