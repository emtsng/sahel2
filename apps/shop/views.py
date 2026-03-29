from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from apps.core.demo_content import SHOP_PRODUCTS, get_by_id


def product_list(request):
    return render(
        request,
        'shop/shop.html',
        {
            'nav_section': 'shop',
            'products': SHOP_PRODUCTS,
            'page_title': 'Shop',
            'breadcrumbs': [{'label': 'Shop'}],
        },
    )


def product_detail(request, pk):
    product = get_by_id(SHOP_PRODUCTS, pk)
    if not product:
        raise Http404('Product not found')
    return render(
        request,
        'shop/shop_detail.html',
        {
            'nav_section': 'shop',
            'product': product,
            'page_title': product['title'],
            'breadcrumbs': [
                {'url': reverse('shop:list'), 'label': 'Shop'},
                {'label': product['title']},
            ],
        },
    )
