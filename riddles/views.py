from django.shortcuts import render
from .models import Book
# Create your views here.
COUNT_OF_BOOKS_ON_PAGE = 24
def toCheckbox(checked):
	if checked == "on":
		return "checked"
	else:
		return ""

def index(request):
	page = request.GET.get("page", "0")
	search = request.GET.get("search", "")

	s_author = request.GET.get("search-author", "off")
	s_name = request.GET.get("search-name", "off")
	s_description = request.GET.get("search-description", "off")

	if search == "":
		all_objects = Book.objects.all()
	else:
		objects_by_name = []
		objects_by_author = []
		objects_by_description = []

		if s_name == "on":
			objects_by_name = Book.objects.filter(name__icontains=search)
		if s_author == "on":
			objects_by_author = Book.objects.filter(author__icontains=search)
		if s_description == "on":
			objects_by_description = Book.objects.filter(description__icontains=search)

		all_objects = []
		all_objects.extend(objects_by_name)
		all_objects.extend(objects_by_author)
		all_objects.extend(objects_by_description)

	filters = {
		"name": toCheckbox(s_name),
		"author": toCheckbox(s_author),
		"description": toCheckbox(s_description),
		"search": search,
		"page": page
	}

	objects = all_objects[0+COUNT_OF_BOOKS_ON_PAGE*int(page):COUNT_OF_BOOKS_ON_PAGE+COUNT_OF_BOOKS_ON_PAGE*int(page)]
	books_count = len(objects)
	pages_count = len(all_objects)/COUNT_OF_BOOKS_ON_PAGE
	data = {"pages_count": pages_count, "books": objects, "books_count": books_count, "filters": filters}

	RENDER = render(request, "riddles/index.html", context=data)
	return RENDER
