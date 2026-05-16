from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from apps.core.demo_content import (
    SERVICE_ITEMS,
    SITE_NAME,
    TEAM_MEMBERS,
)


def home(request):
    hero_slides = [
        {
            'image': 'assets/images/slider/slide-1.jpg',
            'title_before': '',
            'title_span': SITE_NAME,
            'title_after': ' powers energy retail and logistics.',
            'text': (
                'We supply PMS, AGO, DPK, lubricants, and LPG, run dependable transport for liquid, '
                'solid, and grain cargo, and operate a trusted fueling station.'
            ),
        },
    ]
    testimonials = [
        {
            'name': 'Operations Partner',
            'role': 'Fleet and depot customer',
            'image': 'assets/images/testimonial/img-1.jpg',
            'quote': (
                'Sahel Enerlog delivers on schedule and keeps product handling professional from '
                'pickup to final drop.'
            ),
        },
        {
            'name': 'Retail Fuel Buyer',
            'role': 'Commercial customer',
            'image': 'assets/images/testimonial/img-1.jpg',
            'quote': (
                'Their PMS and AGO supply is consistent, and the team communicates clearly about '
                'availability and delivery windows.'
            ),
        },
        {
            'name': 'Logistics Client',
            'role': 'Third-party cargo owner',
            'image': 'assets/images/testimonial/img-1.jpg',
            'quote': (
                'We trust Sahel Enerlog for moving liquid and dry cargo safely. Their turnaround '
                'time has improved our weekly dispatch plan.'
            ),
        },
        {
            'name': 'Station Customer',
            'role': 'Fleet supervisor',
            'image': 'assets/images/testimonial/img-1.jpg',
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
        'hero_slides': hero_slides,
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
