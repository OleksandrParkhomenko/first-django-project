from django import forms

from .models import BlogPost


class BlogPostForm(forms.Form):
	title	= forms.CharField()
	slug	= forms.SlugField()
	content	= forms.CharField(widget=forms.Textarea)



class BlogPostModelForm(forms.ModelForm):
	
	class Meta:
		model 	= BlogPost
		fields	= ['title', 'slug', 'image', 'content', 'publish_date']


	def clean_title(self, *args, **kwargs):
		instance 	= self.instance
		title 		= self.cleaned_data.get('title')
		queryset	= BlogPost.objects.filter(title__iexact=title)
		if instance is not None:
			queryset = queryset.exclude(pk=instance.pk)
		if queryset.exists():
			raise forms.ValidationError("This title has been already used. Please try again.")
		return title

