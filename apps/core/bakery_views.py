from bakery.views import BuildableListView
from django.conf import settings
from fs import path

from apps.core.demo_content import (
    SERVICE_ITEMS,
    SITE_NAME,
    TEAM_MEMBERS,
    get_by_id,
)


def _base_context(**extra):
    ctx = {
        'site_name': SITE_NAME,
    }
    ctx.update(extra)
    return ctx


class HomeView(BuildableListView):
    template_name = 'core/index.html'
    build_path = 'index.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
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
        return _base_context(
            nav_section='home',
            hero_slides=hero_slides,
            services=SERVICE_ITEMS,
            testimonials=testimonials,
            partners=partners,
        )


class AboutView(BuildableListView):
    template_name = 'core/about.html'
    build_path = 'about/index.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        return _base_context(
            nav_section='about',
            page_title='About Us',
            breadcrumbs=[{'label': 'About'}],
            services=SERVICE_ITEMS,
        )


class ContactView(BuildableListView):
    template_name = 'core/contact.html'
    build_path = 'contact/index.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        return _base_context(
            nav_section='contact',
            page_title='Contact',
            breadcrumbs=[{'label': 'Contact'}],
        )


class TeamView(BuildableListView):
    template_name = 'core/team.html'
    build_path = 'about/team/index.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        return _base_context(
            nav_section='team',
            page_title='Our Team',
            breadcrumbs=[
                {'url': '/about/', 'label': 'About'},
                {'label': 'Team'},
            ],
            team_members=TEAM_MEMBERS,
        )
