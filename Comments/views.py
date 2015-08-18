from django.views.generic import FormView, ListView
from django.core.urlresolvers import reverse
from .models import Comment
from .forms import CommentForm


# Create your views here.
class CommentListView(ListView):

    """
    """
    model = Comment
    template_name = "comments/comments.html"


class CommentFormView(FormView):
    form_class = CommentForm
    model = Comment
    template_name = 'comments/comment_form.html'

    def get_success_url(self):
        """
        """
        return reverse('recipe-detail')
