from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import Comment
from .forms import CommentForm


# Create your views here.
class CommentListView(ListView):

    """
    """
    model = Comment
    template_name = "comments/comments.html"

    def get_context_data(self, **kwargs):
        context = super(CommentListView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CommentCreateView(CreateView):
    form_class = CommentForm
    model = Comment
    template_name = 'comments/comment_form.html'
    success_url = reverse_lazy('comment-list')
