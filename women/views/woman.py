from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from women.models import Woman
from ..forms import AddPostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class WomanListView(ListView):
    model = Woman
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = None
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Woman.published.all()


class WomanDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Woman
    template_name = 'women/woman_detail.html'
    title_page = 'Детальная страница',
    permission_required = 'women.view_woman'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class WomanUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Woman
    form_class = AddPostForm
    template_name = 'women/woman_update.html'
    title_page = 'Изменить данный пост'
    success_url = reverse_lazy('women:woman-detail')
    permission_required = 'women.change_woman'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_success_url(self):
        return reverse_lazy('women:woman-detail', kwargs={'pk': self.object.pk})


class WomanCreateView(LoginRequiredMixin, CreateView):
    model = Woman
    form_class = AddPostForm
    template_name = "women/add_post.html"

    def form_valid(self, form):
        woman = form.save(commit=False)
        woman.author = self.request.user
        return super().form_valid(form)
