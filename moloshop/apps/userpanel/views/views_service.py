# moloshop/apps/userpanel/views_service.py

from django.shortcuts import render, get_object_or_404
from apps.core.models import ServicePolicy


def policy_list(request):
    """
    Список всех служебных документов.
    """
    policies = ServicePolicy.objects.all().order_by('-updated_at')
    return render(request, 'userpanel/policies/policy_list.html', {
        'title': 'Служебная информация',
        'policies': policies,
        'current_path': request.path,
    })


def policy_detail(request, slug):
    """
    Детальный просмотр документа.
    """
    policy = get_object_or_404(ServicePolicy, slug=slug)
    return render(request, 'userpanel/policies/policy_detail.html', {
        'title': policy.seo_title or policy.title,
        'policy': policy,
        'seo_description': policy.seo_description,
        'current_path': request.path,
    })
