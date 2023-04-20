from django.db import models

class NewsModel(models.Model):
    title = models.CharField(verbose_name=('Заголовок'),max_length=255)
    body = models.TextField(verbose_name=('Описание'),blank=True, null=True)
    created_date = models.DateTimeField(verbose_name=('Дата'),auto_now_add=True)
    image = models.ImageField(verbose_name=('Изображение'),upload_to='news/images')

    def __str__(self):
        return f'{self.title} | {self.date}'

    def get_full_name(self):
        return f'{self.title} {self.created_date}'

    class Meta:
        ordering = ['-created_date']
        verbose_name = ('Новость')
        verbose_name_plural = ('Новости')
