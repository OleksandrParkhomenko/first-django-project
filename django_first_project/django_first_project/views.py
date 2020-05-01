from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
	title = "Hello there.."
	return render(request, "helloworld.html", {"title" : title})

def about_page(request):
	title = "About us."
	return render(request, "helloworld.html", {"title" : title})

def contact_page(request):
	title = "Contact us."
	return render(request, "helloworld.html", {"title" : title})


def example_page(request):
	context 		= {"title" : "Example"}
	template_name	= "helloworld.html"
	template_obj	= get_template(template_name)
	rendered_item	= template_obj.render(context)
	return HttpResponse(rendered_item)