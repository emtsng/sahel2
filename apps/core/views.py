from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from apps.core.demo_content import (
    SERVICE_ITEMS,
    SITE_NAME,
    TEAM_MEMBERS,
)


def home(request):
    testimonials = [
        {
            'name': 'Operations Partner',
            'role': 'Fleet and depot customer',
            'image': 'assets/images/nigeria/engineer-team.jpg',
            'image_alt': 'Engineers reviewing project plans together',
            'quote': (
                'Sahel Enerlog delivers on schedule and keeps product handling professional from '
                'pickup to final drop.'
            ),
        },
        {
            'name': 'Retail Fuel Buyer',
            'role': 'Commercial customer',
            'image': 'assets/images/nigeria/female-engineer.jpg',
            'image_alt': 'Field engineer carrying out a site survey',
            'quote': (
                'Their PMS and AGO supply is consistent, and the team communicates clearly about '
                'availability and delivery windows.'
            ),
        },
        {
            'name': 'Logistics Client',
            'role': 'Third-party cargo owner',
            'image': 'assets/images/nigeria/field-engineer.jpg',
            'image_alt': 'Engineer in safety gear at an outdoor industrial site',
            'quote': (
                'We trust Sahel Enerlog for moving liquid and dry cargo safely. Their turnaround '
                'time has improved our weekly dispatch plan.'
            ),
        },
        {
            'name': 'Station Customer',
            'role': 'Fleet supervisor',
            'image': 'assets/images/nigeria/engineer-ppe.jpg',
            'image_alt': 'Engineer wearing protective equipment',
            'quote': (
                'The fueling station service is fast and reliable. Product quality and courteous '
                'support keep our drivers coming back.'
            ),
        },
    ]
    partners = [
        {'image': 'assets/images/partners/img-1.png'},
    ]
    context = {
        'nav_section': 'home',
        'services': SERVICE_ITEMS,
        'testimonials': testimonials,
        'partners': partners,
    }
    return render(request, 'core/index.html', context)


def about(request):
    return render(
        request,
        'core/about.html',
        {
            'nav_section': 'about',
            'page_title': 'About Us',
            'breadcrumbs': [{'label': 'About'}],
            'services': SERVICE_ITEMS,
        },
    )


def contact(request):
    return render(
        request,
        'core/contact.html',
        {
            'nav_section': 'contact',
            'page_title': 'Contact',
            'breadcrumbs': [{'label': 'Contact'}],
        },
    )


def team(request):
    return render(
        request,
        'core/team.html',
        {
            'nav_section': 'team',
            'page_title': 'Our Team',
            'breadcrumbs': [
                {'url': reverse('core:about'), 'label': 'About'},
                {'label': 'Team'},
            ],
            'team_members': TEAM_MEMBERS,
        },
    )


def handler404(request, exception):
    return render(request, '404.html', status=404)
