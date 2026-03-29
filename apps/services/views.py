from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from apps.core.demo_content import SERVICE_ITEMS, get_by_id


def service_list(request):
    return render(
        request,
        'services/services.html',
        {
            'nav_section': 'services',
            'services': SERVICE_ITEMS,
            'page_title': 'Services',
            'breadcrumbs': [{'label': 'Services'}],
        },
    )


def service_detail(request, pk):
    item = get_by_id(SERVICE_ITEMS, pk)
    if not item:
        raise Http404('Service not found')
    related = [s for s in SERVICE_ITEMS if s['id'] != int(pk)]
    return render(
        request,
        'services/service_detail.html',
        {
            'nav_section': 'services',
            'service': item,
            'related_services': related,
            'page_title': item['title'],
            'breadcrumbs': [
                {'url': reverse('services:list'), 'label': 'Services'},
                {'label': item['title']},
            ],
        },
    )
