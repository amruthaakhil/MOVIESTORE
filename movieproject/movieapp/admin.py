from django.contrib import admin
from .models import Movie, Review, Rating
from .models import Category

# Register your models here
class MovieAdmin(admin.ModelAdmin):
    list_display=['name','img','desc','release','actors','category','trailer_link']
    list_editable=['img','category','trailer_link']
    prepopulated_fields={'slug':('name',)}
    list_per_page=20
admin.site.register(Movie,MovieAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'review_text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'movie__name']

admin.site.register(Review, ReviewAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'rating_value', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'movie__name']

admin.site.register(Rating, RatingAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name','slug',]
    prepopulated_fields ={'slug':('category_name',)}
admin.site.register(Category,CategoryAdmin)