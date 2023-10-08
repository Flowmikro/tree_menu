from django.db import models


class MenuModel(models.Model):
    """Древовидное меню"""
    name = models.CharField('Название', max_length=150, help_text='Максимум 100 символов')
    named_url = models.CharField('URL', max_length=150, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', help_text='Выберете пункт',
                               verbose_name='Родитель', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name
