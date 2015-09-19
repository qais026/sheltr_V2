from django import forms
from django.forms.formsets import formset_factory
from .models import Post, Category

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ageChildrenForm(forms.Form):
	ageChildrenChoices = (('16oryounger', "16 or younger", "17orolder", "17 or older"))
	questionAgeChildren = forms.ChoiceField(label="How old is each child?", choices=ageChildrenChoices)

class SearchForm(forms.Form):
#	resourceType = forms.ModelMultipleChoiceField(queryset=None, label="Category")

	yesno = (('YES', "Yes"), ('NO', "No"))

	ageChoices = (('Under 18', "Under 18"), ('18-21', "18-21"), ('21-24', "21-24"), ('25-35', "25-35"), ('Above 35', "Above 35"))
	questionAge = forms.ChoiceField(label="How old are you?", choices=ageChoices)

	genderChoices = (('MALE', "Male"), ('FEMALE', "Female"), ('OTHER', 'Other'))
	questionGender = forms.ChoiceField(choices=genderChoices, label="What is your gender?", widget=forms.RadioSelect)

	questionVeteranStatus = forms.ChoiceField(label="Are you a US Military veteran?", choices=yesno, widget=forms.RadioSelect)

	questionChildren = forms.ChoiceField(label="Do you any children accompanying you?", choices=yesno, widget=forms.RadioSelect)

	numChildrenChoices = (('Not Applicable', "Not Applicable"), ('ONE', "One"), ('MORETHANONE', "More than one"))
	questionNumChildren = forms.ChoiceField(label="If you have children, how many are accompanying you?", choices=numChildrenChoices, widget=forms.RadioSelect)

	# ageChildrenFormSet = formset_factory(ageChildrenForm, extra=2)
	# formset = ageChildrenFormSet()


	




	def __init__(self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
	#	self.fields['resourceType'].queryset = Category.objects.all()

