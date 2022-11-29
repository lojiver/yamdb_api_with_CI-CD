from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.expressions import RawSQL
from users.models import User

from .validators import validate_year


class ScoreManager(models.Manager):
    def avg_score(self):
        return self.annotate(rating=RawSQL('''
        select avg(score) from titles_reviews r, titles_title t
        where r.title = t.id
        '''))


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Категория'
    )

    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-id']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Жанр'
    )

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['-id']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название'
    )

    year = models.SmallIntegerField(
        verbose_name='Год выпуска', db_index=True,
        validators=[validate_year]
    )

    description = models.TextField(
        max_length=400,
        verbose_name='Описание',
        null=True,
        blank=True,
    )

    genre = models.ManyToManyField(
        Genre, through='GenreTitle',
        related_name='titles',
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='titles',
    )

    objects = ScoreManager()

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Название'
        ordering = ['-id']

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name='Жанр'
    )

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'Жанр/Название'
        verbose_name_plural = 'Жанры/Названия'

    def __str__(self):
        return f'{self.genre} {self.title}'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор')

    text = models.TextField(
        max_length=400,
        verbose_name='Текст отзыва',
    )

    score = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1, 'Оценка не может быть меньше 1'),
        MaxValueValidator(10, 'Оценка не может быть выше 10')
    ])

    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True, db_index=True
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_title_author'
            )
        ]


class Comments(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Произведение'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор')

    text = models.TextField(
        max_length=400,
        verbose_name='Текст комментария',
    )

    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author}, {self.pub_date}: {self.text}'
