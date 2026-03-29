from django.http import Http404
from django.shortcuts import render

from apps.core.demo_content import (
    BLOG_POSTS,
    PROJECT_ITEMS,
    SERVICE_ITEMS,
    SITE_NAME,
)


def home(request):
    hero_slides = [
        {
            'image': 'assets/images/slider/slide-1.jpg',
            'title_before': 'With ',
            'title_span': SITE_NAME,
            'title_after': ', nothing is impossible.',
            'text': (
                'Industrial excellence, safety, and delivery—Sahel partners with you from concept '
                'to commissioning.'
            ),
        },
    ]
    testimonials = [
        {
            'name': 'Leslie Alexander',
            'role': 'MD, Sahel partner network',
            'image': 'assets/images/testimonial/img-1.jpg',
            'quote': (
                'Sahel brought discipline and clarity to a complex retrofit. Communication stayed '
                'sharp from kickoff to handover.'
            ),
        },
    ]
    team_members = [
        {
            'name': 'Esther Howard',
            'role': 'Creative Director',
            'image': 'assets/images/team/img-1.jpg',
        },
    ]
    partners = [
        {'image': 'assets/images/partners/img-1.png'},
    ]
    context = {
        'nav_section': 'home',
        'hero_slides': hero_slides,
        'services': SERVICE_ITEMS,
        'projects': PROJECT_ITEMS,
        'testimonials': testimonials,
        'team_members': team_members,
        'partners': partners,
        'posts': BLOG_POSTS,
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


def handler404(request, exception):
    return render(request, '404.html', status=404)
