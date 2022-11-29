from django.contrib import admin

from .models import Category, Comments, Genre, GenreTitle, Review, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)


admin.site.register(Genre, GenreAdmin)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year',)
    search_fields = ('name',)


admin.site.register(Title, TitleAdmin)


class GenreTitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'genre')
    search_fields = ('title', 'genre')


admin.site.register(GenreTitle, GenreTitleAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'score')
    search_fields = ('text',)


admin.site.register(Review, ReviewsAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text')
    search_fields = ('text',)


admin.site.register(Comments, CommentsAdmin)
