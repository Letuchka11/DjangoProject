from django.db import models


# Create your models here.

class Director(models.Model):
    class Meta:
        verbose_name = 'Режиссерa'
        verbose_name_plural = 'Режиссеры'
    name = models.CharField(max_length=70, verbose_name='Режиссер')

    def __str__(self):        return self.name

class Films(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-rating', 'title']

    director = models.ForeignKey(Director, on_delete=models.PROTECT,
                                 related_name="director" , null=True,
                                 verbose_name='Режиссёр')

    title = models.CharField(max_length=250 ,
                             verbose_name='Название')

    producer = models.CharField(max_length=250,
                                verbose_name='Продюссер')

    rating = models.FloatField(verbose_name='Рейтинг')

    duration = models.IntegerField(verbose_name='Длительность')

    created = models.DateTimeField(auto_now_add=True, null=True,
                                   verbose_name='Дата создания')

    updated = models.DateTimeField(auto_now=True, null=True,
                                   verbose_name='Дата обновления')

    def __str__(self):
        return self.title
