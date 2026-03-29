"""Placeholder content until CMS/models exist. Each list is intentionally single-item."""

SITE_NAME = 'Sahel'

SERVICE_ITEMS = [
    {
        'id': 1,
        'title': 'Mechanical Engineering',
        'icon': 'assets/images/icon/engineering.svg',
        'excerpt': 'Consectetur adipiscing elit. Expert industrial solutions tailored by Sahel.',
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
        'title': 'Chemical Refinery',
        'label': '01',
        'image': 'assets/images/projects/1.jpg',
        'hero_images': (
            'assets/images/project-single/1.jpg',
        ),
        'tagline': 'Recent Project',
        'client': 'Sahel',
        'location': '7 Lake Street, London',
        'meta': [
            ('Location', '7 Lake Street, London'),
            ('Client', 'Sahel'),
            ('Architect', 'Sahel Studio'),
            ('Project Type', 'Industrial'),
            ('Duration', '6 Month'),
            ('Completion', '15 Apr 2022'),
            ('Share', 'Industrial, Business'),
        ],
        'gallery': (
            'assets/images/project-single/2.jpg',
            'assets/images/project-single/3.jpg',
        ),
    },
]

BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Why Industry Is a Juicy Target for Cyberattack.',
        'excerpt': 'Industrial operations need resilient systems. Sahel outlines what to watch for.',
        'author': 'Sahel Editorial',
        'date_display': '24 Jun 2022',
        'comments': 5,
        'image': 'assets/images/blog/img-4.jpg',
        'body_lead': (
            'There are many variations of passages available, but the majority have suffered '
            'alteration in some form. Sahel helps teams build practical security habits.'
        ),
    },
]

SHOP_PRODUCTS = [
    {
        'id': 1,
        'title': 'Industrial grade miter saw',
        'image': 'assets/images/shop/1.jpg',
        'price_old': '$230.00',
        'price': '$220.00',
        'thumb_main': 'assets/images/shop/shop-single/1.jpg',
        'thumbs': (
            'assets/images/shop/shop-single/thumb/img-1.jpg',
        ),
    },
]

FOOTER_SERVICES = [
    {'id': 1, 'title': 'Mechanical Engineering'},
]


def get_by_id(items, pk):
    for item in items:
        if item['id'] == int(pk):
            return item
    return None
