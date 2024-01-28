from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    preview = models.ImageField(upload_to='media/', verbose_name='Превью курса', **NULLABLE)
    description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название урока')
    description_lesson = models.CharField(max_length=200, verbose_name='Описание урока')
    preview_lesson = models.ImageField(upload_to='media/', verbose_name='Превью урока', **NULLABLE)
    link = models.CharField(max_length=200, verbose_name='Ссылка на урок')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
