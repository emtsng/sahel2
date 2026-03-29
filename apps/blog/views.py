from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from apps.core.demo_content import BLOG_POSTS, get_by_id


def post_list(request):
    return render(
        request,
        'blog/blog.html',
        {
            'nav_section': 'blog',
            'posts': BLOG_POSTS,
            'page_title': 'Latest News',
            'breadcrumbs': [{'label': 'Blog'}],
        },
    )


def post_detail(request, pk):
    post = get_by_id(BLOG_POSTS, pk)
    if not post:
        raise Http404('Post not found')
    comments = [
        {
            'author': 'Robert Sonny',
            'date': 'Jul 21, 2022 at 10:00am',
            'image': 'assets/images/blog-details/comments-author/img-1.jpg',
            'body': (
                'Clear, actionable perspective—exactly what we needed while planning our plant '
                'upgrade with Sahel.'
            ),
        },
    ]
    return render(
        request,
        'blog/blog_detail.html',
        {
            'nav_section': 'blog',
            'post': post,
            'comments': comments,
            'page_title': post['title'],
            'breadcrumbs': [
                {'url': reverse('blog:list'), 'label': 'Blog'},
                {'label': post['title']},
            ],
        },
    )
