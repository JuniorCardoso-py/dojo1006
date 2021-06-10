from django.db import models


class Marketplace(models.Model):

    name = models.CharField('nome', max_length=150)
    description = models.CharField('descrição', max_length=255)
    phone = models.CharField('telefone', max_length=14)
    email = models.EmailField('email', max_length=120)
    website = models.URLField('site', blank=True)

    def __str__(self):
        return self.name


class Configuration(models.Model):

    configurator = models.ForeignKey('Marketplace', on_delete=models.CASCADE,
                                     related_name='marketplace')
    endpoint = models.URLField('endpoint')
    secret_key = models.CharField('secret_key', max_length=255)
    api = models.URLField('api')

    def __str__(self):
        return self.endpoint
