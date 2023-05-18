from django.db import models

class ServiceModel(models.Model):
    title = models.CharField(verbose_name=('Заголовок'),max_length=255)
    image = models.ImageField(verbose_name=('Изображение'),upload_to='news/images')

    def __str__(self):
        return f'{self.title}'


    class Meta:
        verbose_name = ('Сервис')
        verbose_name_plural = ('Сервисы')
