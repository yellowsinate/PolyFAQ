from django.db import models

# Create your models here.

class FAQ(models.Model):
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return self.question

class Article(models.Model):
    header = models.TextField(verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    tag = []

    def __str__(self):
        return self.header