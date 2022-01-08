from django.db import models


class GuestBookRecord(models.Model):

    STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]

    author = models.CharField(max_length=50, verbose_name='Автор')
    email = models.EmailField(max_length=50, verbose_name='Email')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name='Статус')

    def __str__(self):
        return f"{self.pk}. {self.author}: {self.status}"

    class Meta:
        db_table = 'records'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
