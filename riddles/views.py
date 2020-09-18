from django.shortcuts import render
from .models import Book
# Create your views here.
COUNT_OF_BOOKS_ON_PAGE = 24
def index(request):
	page = request.GET.get("page", "0")
	search = request.GET.get("search", "")

	if search == "":
		all_objects = Book.objects.all()
	else:
		objects_by_name = Book.objects.filter(name__icontains=search)
		objects_by_author = Book.objects.filter(author__icontains=search)
		all_objects = []
		all_objects.extend(objects_by_name)
		all_objects.extend(objects_by_author)
	objects = all_objects[0+COUNT_OF_BOOKS_ON_PAGE*int(page):COUNT_OF_BOOKS_ON_PAGE+COUNT_OF_BOOKS_ON_PAGE*int(page)]
	books_count = len(objects)
	pages_count = len(all_objects)/COUNT_OF_BOOKS_ON_PAGE
	data = {"pages_count": pages_count, "books": objects, "books_count": books_count}
	return render(request, "riddles/index.html", context=data)
