"""Demo content used by templates before dynamic CMS data is available."""

SITE_NAME = 'Sahel Enerlog'

SERVICE_ITEMS = [
    {
        'id': 1,
        'title': 'Energy Product Retail',
        'icon': 'assets/images/icon/engineering.svg',
        'excerpt': (
            'Reliable supply and retailing of PMS, AGO, DPK, lubricants, and LPG '
            'for homes, fleets, and industrial users.'
        ),
        'hero_image': 'assets/images/service-single/1.jpg',
        'gallery': (
            'assets/images/service-single/2.jpg',
            'assets/images/service-single/3.jpg',
        ),
    },
    {
        'id': 2,
        'title': 'Energy and Cargo Logistics',
        'icon': 'assets/images/icon/engineering.svg',
        'excerpt': (
            'End-to-end transportation for petroleum products and third-party cargo, '
            'including liquid, solid, and grain shipments.'
        ),
        'hero_image': 'assets/images/service-single/1.jpg',
        'gallery': (
            'assets/images/service-single/2.jpg',
            'assets/images/service-single/3.jpg',
        ),
    },
    {
        'id': 3,
        'title': 'Fueling Station Operations',
        'icon': 'assets/images/icon/engineering.svg',
        'excerpt': (
            'Safe and customer-focused fueling station services with dependable pump '
            'availability and quality-controlled products.'
        ),
        'hero_image': 'assets/images/service-single/1.jpg',
        'gallery': (
            'assets/images/service-single/2.jpg',
            'assets/images/service-single/3.jpg',
        ),
    },
]

PROJECT_ITEMS = [
    {
        'id': 1,
        'title': 'Retail Fuel Supply Program',
        'label': '01',
        'image': 'assets/images/projects/1.jpg',
        'hero_images': (
            'assets/images/project-single/1.jpg',
        ),
        'tagline': 'Energy Retail',
        'client': 'Commercial and residential buyers',
        'location': 'Multi-city supply network',
        'meta': [
            ('Location', 'Multi-city supply network'),
            ('Client', 'Commercial and residential buyers'),
            ('Scope', 'PMS, AGO, DPK, lubricant and LPG retail'),
            ('Project Type', 'Energy distribution'),
            ('Duration', 'Ongoing operations'),
            ('Delivery Model', 'Scheduled and on-demand dispatch'),
            ('Priority', 'Product quality and availability'),
        ],
        'gallery': (
            'assets/images/project-single/2.jpg',
            'assets/images/project-single/3.jpg',
        ),
    },
    {
        'id': 2,
        'title': 'Bulk Logistics and Haulage Service',
        'label': '02',
        'image': 'assets/images/projects/2.jpg',
        'hero_images': (
            'assets/images/project-single/1.jpg',
        ),
        'tagline': 'Logistics',
        'client': 'Energy marketers and third-party cargo owners',
        'location': 'Regional transport corridors',
        'meta': [
            ('Location', 'Regional transport corridors'),
            ('Client', 'Energy marketers and cargo owners'),
            ('Scope', 'Liquid, solid and grain cargo movement'),
            ('Project Type', 'Logistics and transport'),
            ('Duration', 'Year-round service'),
            ('Fleet Focus', 'Safety, tracking and timely delivery'),
            ('Coverage', 'Intercity and depot-to-site routes'),
        ],
        'gallery': (
            'assets/images/project-single/2.jpg',
            'assets/images/project-single/3.jpg',
        ),
    },
    {
        'id': 3,
        'title': 'Company-Owned Fueling Station',
        'label': '03',
        'image': 'assets/images/projects/3.jpg',
        'hero_images': (
            'assets/images/project-single/1.jpg',
        ),
        'tagline': 'Station Operations',
        'client': 'Walk-in motorists and fleet operators',
        'location': 'Local service hub',
        'meta': [
            ('Location', 'Local service hub'),
            ('Client', 'Walk-in motorists and fleet operators'),
            ('Scope', 'Retail dispensing and station support'),
            ('Project Type', 'Fuel station management'),
            ('Duration', 'Daily operations'),
            ('Safety', 'Pump protocol and quality assurance'),
            ('Goal', 'Fast service and trusted supply'),
        ],
        'gallery': (
            'assets/images/project-single/2.jpg',
            'assets/images/project-single/3.jpg',
        ),
    },
]

TEAM_MEMBERS = [
    {
        'name': 'Amina Yusuf',
        'role': 'Managing Director',
        'image': 'assets/images/team/img-1.jpg',
    },
    {
        'name': 'Tunde Adewale',
        'role': 'Head of Logistics',
        'image': 'assets/images/team/img-1.jpg',
    },
    {
        'name': 'Grace Okafor',
        'role': 'Fuel Station Operations Lead',
        'image': 'assets/images/team/img-1.jpg',
    },
    {
        'name': 'Ibrahim Musa',
        'role': 'Supply and Distribution Supervisor',
        'image': 'assets/images/team/img-1.jpg',
    },
]

FOOTER_SERVICES = [
    {'id': 1, 'title': 'Energy Product Retail'},
    {'id': 2, 'title': 'Energy and Cargo Logistics'},
    {'id': 3, 'title': 'Fueling Station Operations'},
]


def get_by_id(items, pk):
    for item in items:
        if item['id'] == int(pk):
            return item
    return None
