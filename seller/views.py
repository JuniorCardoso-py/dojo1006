from seller.forms import SellerForm
from django.shortcuts import redirect, render
from seller.models import Seller


def seller(request):
    sellers = Seller.objects.all()
    return render(request, 'seller.html', {'sellers': sellers})


def seller_create(request):
    seller_form = SellerForm(request.POST or None)
    if seller_form.is_valid():
        seller_form.save()
        return redirect('seller')

    context = {'seller_form': seller_form}
    return render(request, 'seller_form.html', context)
