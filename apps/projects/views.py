from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from apps.core.demo_content import PROJECT_ITEMS, get_by_id


def project_list(request):
    return render(
        request,
        'projects/projects.html',
        {
            'nav_section': 'projects',
            'projects': PROJECT_ITEMS,
            'page_title': 'Projects',
            'breadcrumbs': [{'label': 'Projects'}],
        },
    )


def project_detail(request, pk):
    item = get_by_id(PROJECT_ITEMS, pk)
    if not item:
        raise Http404('Project not found')
    return render(
        request,
        'projects/project_detail.html',
        {
            'nav_section': 'projects',
            'project': item,
            'page_title': item['title'],
            'breadcrumbs': [
                {'url': reverse('projects:list'), 'label': 'Projects'},
                {'label': item['title']},
            ],
        },
    )
