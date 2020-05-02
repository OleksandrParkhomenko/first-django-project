from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


from .forms import ContactForm

def home_page(request):
	title 	= "Hello there.."
	context = {"title" : title}
	return render(request, "home.html", context)

def about_page(request):
	title 	= "About us."
	return render(request, "helloworld.html", {"title" : title})

def contact_page(request):
	title 	= "Contact us."
	form 	= ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context	= {
		"title" : title,
		"form" 	: form
	}
	return render(request, "form.html", context)


def example_page(request):
	context 		= {"title" : "Example"}
	template_name	= "helloworld.html"
	template_obj	= get_template(template_name)
	rendered_item	= template_obj.render(context)
	return HttpResponse(rendered_item)