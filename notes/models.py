from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Note(models.Model):
    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Note, self).save(*args, **kwargs)

    class meta:
        ordering = ('-created',)
