from bakery.views import BuildableDetailView, BuildableListView
from django.conf import settings
from django.http import Http404
from fs import path

from apps.core.demo_content import SERVICE_ITEMS, get_by_id


class ServiceListView(BuildableListView):
    template_name = 'services/services.html'
    build_path = 'services/index.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        return {
            'nav_section': 'services',
            'services': SERVICE_ITEMS,
            'page_title': 'Services',
            'breadcrumbs': [{'label': 'Services'}],
        }


class ServiceDetailView(BuildableDetailView):
    template_name = 'services/service_detail.html'

    def get_queryset(self):
        return SERVICE_ITEMS

    def get_object(self, queryset=None):
        item = get_by_id(SERVICE_ITEMS, self.kwargs.get('pk'))
        if not item:
            raise Http404('Service not found')
        return item

    def get_build_path(self):
        return f'services/{self.kwargs.get("pk")}.html'

    def build_queryset(self):
        # Override to handle list instead of QuerySet
        for item in self.get_queryset():
            self.kwargs = {'pk': item['id']}
            self.object = self.get_object()
            # Prepare request and directory, then write the built file
            self.request = self.create_request(self.get_build_path())
            self.prep_directory(self.get_build_path())
            target_path = path.join(settings.BUILD_DIR, self.get_build_path())
            self.build_file(target_path, self.get_content())

    def get_context_data(self, **kwargs):
        item = self.object
        related = [s for s in SERVICE_ITEMS if s['id'] != int(self.kwargs.get('pk'))]
        return {
            'nav_section': 'services',
            'service': item,
            'related_services': related,
            'page_title': item['title'],
            'breadcrumbs': [
                {'url': '/services/', 'label': 'Services'},
                {'label': item['title']},
            ],
        }
