from authors.models import Profile
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'authors/pages/profile.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        profile_id = context.get('id')
        profile = get_object_or_404(Profile.objects.filter(
            pk=profile_id
        ).select_related('author'), pk=profile_id)

        return self.render_to_response({
            **context,
            'profile': profile,
        })
