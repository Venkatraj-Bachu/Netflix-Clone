from django.contrib import admin
from .models import Movie, Originals, TopRatedMovie

# Register your models here.
admin.site.register(Movie)
admin.site.register(Originals)
admin.site.register(TopRatedMovie)