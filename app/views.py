from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	# Example filter, display "posts" which is Post from a certain timezone and ordered by date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/post_list.html', {'posts':posts})