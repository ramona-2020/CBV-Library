from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Author(models.Model):
    AUTHOR_NAME_MAX_LENGTH = 10

    name = models.CharField(max_length=AUTHOR_NAME_MAX_LENGTH)

    def __str__(self):
        return self.name


class Book(models.Model):
    BOOK_TITLE_MAX_LENGTH = 60

    ACTION = 'Action'
    THRILLER = 'Thriller'
    COMEDI = 'Comedi'

    GENRES = [(c, c) for c in (ACTION, THRILLER, COMEDI)]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=BOOK_TITLE_MAX_LENGTH)

    pages = models.IntegerField()
    code = models.IntegerField()

    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True)

    genre = models.CharField(
        max_length=max(len(c) for (c, _) in GENRES),
        choices=GENRES)

    date_published = models.DateField(
        null=True,
        blank=True,
        auto_now_add=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def __str__(self):
        return "%s - %s - %s - %s" % (self.title, self.author.name, self.code, self.pages)
