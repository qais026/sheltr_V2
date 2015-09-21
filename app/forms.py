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

	yesno = (('YES', "Yes"), ('NO', "No"))
	yesnona = ( ('NA', "Not Applicable"), ('YES', "Yes"), ('NO', "No"),)
	ageChoices = (('Under 18', "Under 18"), ('18-21', "18-21"), ('21-24', "21-24"), ('25-35', "25-35"), ('Above 35', "Above 35"))
	questionAge = forms.ChoiceField(label="How old are you?", choices=ageChoices, required=False)

	genderChoices = (('MALE', "Male"), ('FEMALE', "Female"), ('OTHER', 'Other'))
	questionGender = forms.ChoiceField(label="What is your gender?", 
		choices=genderChoices, required=False, widget=forms.RadioSelect)

	questionVeteranStatus = forms.ChoiceField(label="Are you a US Military veteran?", 
		choices=yesno, required=False, widget=forms.RadioSelect)

	questionChildren = forms.ChoiceField(label="Do you any children accompanying you?", 
		choices=yesno, required=False, widget=forms.RadioSelect)

	numChildrenChoices = (('Not Applicable', "Not Applicable"), ('ONE', "One"), ('MORETHANONE', "More than one"))
	questionNumChildren = forms.ChoiceField(label="If you have children, how many are accompanying you?", 
		choices=numChildrenChoices, required=False)

	ageChildrenChoices = (('Younger16', "16 or younger"), ('Older17', "17 or older"))
	questionAgeChildren = forms.MultipleChoiceField(label="If you have children, what are the ages of the children?",
		choices=ageChildrenChoices, required=False, widget=forms.CheckboxSelectMultiple)

	questionCriminal = forms.ChoiceField(label="Have you been incarcerated?",
		choices=yesno, required=False, widget=forms.RadioSelect)

	questionSubstanceAbuse = forms.ChoiceField(label="Are you currently challenged with substance abuse?",
		choices=yesno, required=False, widget=forms.RadioSelect)

	questionHIV = forms.ChoiceField(label="Have you tested positive for HIV?",
		choices=yesno, required=False, widget=forms.RadioSelect)

	questionMentalStatus = forms.ChoiceField(label="Have you been diagnosed with a mental health condition?",
		choices=yesno, required=False, widget=forms.RadioSelect)

	questionDisability = forms.ChoiceField(label="Do you have a physical disability?",
		choices=yesno, required=False, widget=forms.RadioSelect)

	# questionWheelChair = forms.ChoiceField(label="If you a physical disability, do you have a wheelchair?",
	# 	choices=yesnona, required=False)	

	def __init__(self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
	#	self.fields['resourceType'].queryset = Category.objects.all()

