from django.db import models

# Create your models here.


class Address(models.Model):

    state = models.CharField(verbose_name='estado', max_length=50)
    city = models.CharField(verbose_name='cidade', max_length=50)
    district = models.CharField(verbose_name='bairro', max_length=50)
    street = models.CharField(verbose_name='rua', max_length=50)
    number = models.IntegerField(verbose_name='numero')
    seller = models.ForeignKey(
        'Seller', related_name='address', on_delete=models.CASCADE)


class Seller(models.Model):

    name = models.CharField(verbose_name='nome', max_length=50)
    cpf = models.CharField(verbose_name='cpf', max_length=11)
    email = models.EmailField(verbose_name='email')
    celphone = models.CharField(verbose_name='telefone', max_length=50)
    # address = models.OneToOneField(Address, on_delete=models.CASCADE, verbose_name='endereco',default=1)
    address = models.ManyToOneRel(
        'seller', to=Address, field_name=None, on_delete=models.CASCADE)
    #   models.OneToOneRel()


# seller1 = Seller()
# seller1.address.all()
