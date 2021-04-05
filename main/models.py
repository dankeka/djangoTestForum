from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
  title = models.CharField('Название', max_length=60, unique=True)
  date = models.DateTimeField('Дата создания', auto_now_add=True)
  
  class Meta:
    verbose_name = 'Секция'
    verbose_name_plural = 'Секции'
    ordering = ['-date']
    
  def __str__(self):
    return self.title

class Theme(models.Model):
  title = models.CharField('Название', max_length=100)
  user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
  section = models.ForeignKey(Section, on_delete=models.PROTECT, verbose_name='Секция')
  date = models.DateTimeField('Дата создания', auto_now_add=True)
  
  class Meta:
    verbose_name = 'Тема'
    verbose_name_plural = 'Темы'
    ordering = ['-date']
    
  def __str__(self):
    return self.title
  
class Message(models.Model):
  text = models.TextField('Тект')
  user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Сообщение')
  date = models.DateTimeField('Дата создания', auto_now_add=True)
  
  class Meta:
    verbose_name = 'Сообщение'
    verbose_name_plural = 'Сообщения'
    ordering = ['-date']
    
  def __str__(self):
    return self.user