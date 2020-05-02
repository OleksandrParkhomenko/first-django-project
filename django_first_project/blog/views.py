from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm



def blog_post_list_view(request):
	# list of objects
	# could be search
	#queryset = BlogPost.objects.all()
	queryset = BlogPost.objects.filter(title__icontains='hello')
	template_name	= 'blog_post_list.html'
	context		 	= {'object_list' : queryset}
	return render(request, template_name, context)


@login_required
def blog_post_create_view(request):
	form = BlogPostModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		form	= BlogPostModelForm()
	template_name	= 'blog/form.html'
	context			= {'form' : form}
	return render(request, template_name, context)



def blog_post_detail_view(request, slug):  
	obj 			= get_object_or_404(BlogPost, slug=slug)
	template_name 	= "blog/detail.html"
	context 		= {"object" : obj}
	return render(request, template_name, context)



def blog_post_update_view(request, slug):
	obj 			= get_object_or_404(BlogPost, slug=slug)
	template_name 	= "blog/update.html"
	context 		= {"object" : obj, 'form' : None}
	return render(request, template_name, context)



def blog_post_delete_view(request, slug):
	obj 			= get_object_or_404(BlogPost, slug=slug)
	template_name 	= "blog/delete.html"
	context 		= {"object" : obj}
	return render(request, template_name, context)