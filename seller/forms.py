from django.forms import ModelForm
from seller.models import Seller


class SellerForm(ModelForm):

    class Meta:
        model = Seller
        fields = ['name', 'cpf', 'email', 'celphone']
