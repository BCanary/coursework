from django.shortcuts import render
from .models import Book
# Create your views here.
COUNT_OF_BOOKS_ON_PAGE = 24
def index(request):
	page = request.GET.get("page", "0")
	search = request.GET.get("search", "")

	all_objects = Book.objects.all()
	objects = all_objects[0+COUNT_OF_BOOKS_ON_PAGE*int(page):COUNT_OF_BOOKS_ON_PAGE+COUNT_OF_BOOKS_ON_PAGE*int(page)]
	books_count = len(objects)
	pages_count = len(all_objects)/COUNT_OF_BOOKS_ON_PAGE
	data = {"pages_count": pages_count, "books": objects, "books_count": books_count}
	return render(request, "riddles/index.html", context=data)
