from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category, Provider
from .forms import PostForm, SearchForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'app/home.html', {})

def post_list(request):
	# Example filter, display "posts" which is Post from a certain timezone and ordered by date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('app.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'app/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('app.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'app/post_edit.html', {'form': form})

def search(request):
    sqs = Provider.objects.all()
    category_list = Category.objects.all()
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
  #          category=form.cleaned_data['resourceType']
  #          sqs = sqs.filter(category=category)

            if form.cleaned_data['questionAge'] == 'Under 18':
                sqs = sqs.filter(category__slug='under_18')

            if form.cleaned_data['questionGender'] == "MALE":
                sqs = sqs.filter(category__name='male')
            elif form.cleaned_data['questionGender'] == "FEMALE":
                sqs = sqs.filter(category__slug='female')









            

    else:
        form = SearchForm() 
    form = SearchForm
    context_dict = {'categories': category_list,
        'form': form,
        'providers': sqs}
    return render(request, 'app/search.html', context_dict)

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated providers.
        # Note that filter returns >= 1 model instance.
        providers = Provider.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['providers'] = providers
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'app/category.html', context_dict)

        # About Us page view
def about(request):
    context_dict = {}
    return render(request, 'app/about.html', context_dict)

        # Project Housing Connect page view
def PHC(request):
    context_dict = {}
    return render(request, 'app/phc.html', context_dict)
