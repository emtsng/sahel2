from apps.core.demo_content import FOOTER_SERVICES, SITE_NAME


def site(request):
    return {
        'site_name': SITE_NAME,
        'footer_services': FOOTER_SERVICES,
    }
