from bakery.views import BuildableDetailView, BuildableListView
from django.conf import settings
from django.http import Http404
from fs import path

from apps.core.demo_content import PROJECT_ITEMS, get_by_id


class ProjectListView(BuildableListView):
    template_name = 'projects/projects.html'
    build_path = 'projects/index.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        return {
            'nav_section': 'projects',
            'projects': PROJECT_ITEMS,
            'page_title': 'Projects',
            'breadcrumbs': [{'label': 'Projects'}],
        }


class ProjectDetailView(BuildableDetailView):
    template_name = 'projects/project_detail.html'

    def get_queryset(self):
        return PROJECT_ITEMS

    def get_object(self, queryset=None):
        item = get_by_id(PROJECT_ITEMS, self.kwargs.get('pk'))
        if not item:
            raise Http404('Project not found')
        return item

    def get_build_path(self):
        return f'projects/{self.kwargs.get("pk")}.html'

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
        return {
            'nav_section': 'projects',
            'project': item,
            'page_title': item['title'],
            'breadcrumbs': [
                {'url': '/projects/', 'label': 'Projects'},
                {'label': item['title']},
            ],
        }
