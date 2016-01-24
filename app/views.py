from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category, Provider
from .forms import PostForm, SearchForm
from django.shortcuts import redirect
from django.db.models import Q
from django.core import serializers
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D

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
    query = False
    sqs = Provider.objects.all()
    category_list = Category.objects.all()
    if request.method == "GET":
        if ('csrfmiddlewaretoken' in request.GET):
            query = True
        form = SearchForm(request.GET)
        if form.is_valid():

            """ AGE """
            if form.cleaned_data['questionAge'] == 'Under 18':
                sqs = sqs.exclude(Q(category__name='age_matters') & ~Q(category__name='under_18'))
            elif form.cleaned_data['questionAge'] == '18-21':
                sqs = sqs.exclude(Q(category__name='age_matters') & ~Q(category__name='18_to_21'))
            elif form.cleaned_data['questionAge'] == '21-24':
                sqs = sqs.exclude(Q(category__name='age_matters') & ~Q(category__name='21_to_24'))
            elif form.cleaned_data['questionAge'] == '25-35':
                sqs = sqs.exclude(Q(category__name='age_matters') & ~Q(category__name='25_35'))
            elif form.cleaned_data['questionAge'] == 'Above 35':
                sqs = sqs.exclude(Q(category__name='age_matters') & ~Q(category__name='above_35'))
 
            """ GENDER """
            if form.cleaned_data['questionGender'] == "MALE":
                sqs = sqs.exclude(Q(category__name='gender') & ~Q(category__name='male'))
            elif form.cleaned_data['questionGender'] == "FEMALE":
                sqs = sqs.exclude(Q(category__name='gender') & ~Q(category__name='female'))
            elif form.cleaned_data['questionGender'] == "OTHER":
                sqs = sqs.exclude(Q(category__name='gender') & ~Q(category__name='other_(transgender,_etc.)'))

            """ VETERAN STATUS """
            if form.cleaned_data['questionVeteranStatus'] == "YES":
                sqs = sqs.exclude(Q(category__name='veteran_status_matters') & ~Q(category__name='veteran_status'))
            elif form.cleaned_data['questionVeteranStatus'] == "NO":
                sqs = sqs.exclude(Q(category__name='veteran_status_matters') & Q(category__name='veteran_status'))
            
            """ CHILDREN """
            if form.cleaned_data['questionChildren'] == "YES":
                sqs = sqs.exclude(Q(category__name='children_matter') & ~Q(category__name='have_children'))
            elif form.cleaned_data['questionChildren'] == "NO":
                sqs = sqs.exclude(Q(category__name='children_matter') & Q(category__name='have_children'))

            """ # CHILDREN """
            if form.cleaned_data['questionNumChildren'] == "ONE":
                sqs = sqs.exclude(Q(category__name='children_number_matters') & Q(category__name='children_num=more_than_1'))
            elif form.cleaned_data['questionNumChildren'] == "MORETHANONE":
                sqs = sqs.exclude(Q(category__name='children_number_matters') & Q(category__name='children_num=1'))

            """ AGE OF CHILDREN """
            younger16 = False
            older17 = False
            for age in form.cleaned_data['questionAgeChildren']:
                if (age == 'Younger16'):   
                    younger16 = True
                elif (age == 'Older17'):
                    older17 = True
            if (younger16 and (older17 == False)):
                sqs = sqs.exclude(Q(category__name='children_age_matters') & ~Q(category__name='children_age16'))
            elif ((younger16 == False) and older17):
                sqs = sqs.exclude(Q(category__name='children_age_matters') & ~Q(category__name='children_age17'))


            """ CRIMINAL RECORD """
            if form.cleaned_data['questionCriminal'] == "YES":
                sqs = sqs.exclude(Q(category__name='criminal_record_matters') & ~Q(category__name='criminal_record'))
            elif form.cleaned_data['questionCriminal'] == "NO":
                sqs = sqs.exclude(Q(category__name='criminal_record_matters') & Q(category__name='criminal_record'))

            """ SUBSTANCE ABUSE """
            if form.cleaned_data['questionSubstanceAbuse'] == "YES":
                sqs = sqs.exclude(Q(category__name='substance_abuse_matters') & ~Q(category__name='substance_abuse'))
            elif form.cleaned_data['questionSubstanceAbuse'] == "NO":
                sqs = sqs.exclude(Q(category__name='substance_abuse_matters') & Q(category__name='substance_abuse'))

            """ HIV """
            if form.cleaned_data['questionHIV'] == "YES":
                sqs = sqs.exclude(Q(category__name='hiv_status_matters') & ~Q(category__name='hiv_status'))
            elif form.cleaned_data['questionHIV'] == "NO":
                sqs = sqs.exclude(Q(category__name='hiv_status_matters') & Q(category__name='hiv_status'))

            """ MENTAL STATUS """
            if form.cleaned_data['questionMentalStatus'] == "YES":
                sqs = sqs.exclude(Q(category__name='mental_health_matters') & ~Q(category__name='mental_health'))
            elif form.cleaned_data['questionMentalStatus'] == "NO":
                sqs = sqs.exclude(Q(category__name='mental_health_matters') & Q(category__name='mental_health'))

            """ DISABILITY STATUS """
            if form.cleaned_data['questionDisability'] == "YES":
                sqs = sqs.exclude(Q(category__name='_') & ~Q(category__name='disability'))
            elif form.cleaned_data['questionDisability'] == "NO":
                sqs = sqs.exclude(Q(category__name='_') & Q(category__name='disability'))  
    else:
        form = SearchForm() 
    form = SearchForm



    ref_loc = Point(39.228796, -76.612263, srid=3857)
    distance = 10000
    geosqs = Provider.gis.all().distance(ref_loc).order_by('distance')
    providers_json = serializers.serialize("json", geosqs, fields=('provider_name', 'latlng'))

    context_dict = {'categories': category_list,
        'form': form,
        'length': sqs.count(),
        'providers': geosqs,
        'query': query,
        'providers_json': providers_json,}
    return render(request, 'app/search.html', context_dict)

def results(request):

    context_dict = {'providers': sqs}
    return render(request, 'app/results.html', context_dict)

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
