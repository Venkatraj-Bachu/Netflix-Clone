from django.db import models
import uuid

GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('science_fiction', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
    ]

# Create your models here.
class Movie(models.Model):

    uu_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to='movie_images/')
    image_cover = models.ImageField(upload_to='movie_images/')
    video = models.FileField(upload_to='movie_videos/')
    movie_views = models.IntegerField(default=0)
    link = models.TextField(default='')

    def __str__(self):
        return self.title
    
class Originals(models.Model):

    uu_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to='original_images/')
    image_cover = models.ImageField(upload_to='original_images/')
    video = models.FileField(upload_to='original_videos/')
    movie_views = models.IntegerField(default=0)
    link = models.TextField(default='')

    def __str__(self):
        return self.title
    
class TopRatedMovie(models.Model):

    uu_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to='top_rated_images/')
    image_cover = models.ImageField(upload_to='top_rated_images/')
    video = models.FileField(upload_to='top_rated_videos/')
    movie_views = models.IntegerField(default=0)
    link = models.TextField(default='')

    def __str__(self):
        return self.title