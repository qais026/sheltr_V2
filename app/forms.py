from django import forms

from .models import Post, Category

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class SearchForm(forms.Form):
	resourceType = forms.ModelMultipleChoiceField(queryset=None, label="Category")
	questionOneChoices = (('YES', "Yes"), ('NO', "No"),)
	questionOne = forms.ChoiceField(choices=questionOneChoices, label="Online only?")
	def __init__(self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
		self.fields['resourceType'].queryset = Category.objects.all()
