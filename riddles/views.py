from django.shortcuts import render
from .models import Book
from bs4 import BeautifulSoup
import os

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

def tag(text):
	return "<" + text + ">"
def ctag(text):
	return "</" + text + ">"

def book_index(request, book_id=1):
	page = request.GET.get("page", "0")

	book = Book.objects.get(id=book_id)

	text = ""
	with open("C:/Users/vladi/Desktop/coursework/riddles/books/book" + str(book_id) + ".fb2", "r", encoding='utf-8') as file:
		#content = file.readlines()
		# Combine the lines in the list into a string
		#content = "".join(content)

		file = file.read()
		file = file.replace("body", "bodyz")
		#print(file)
		bs = BeautifulSoup(file, "lxml")

		text = bs.find("bodyz")
		try:
			section_title = text.title.prettify()
		except:
			section_title = "<h2>" + book.name + "</h2>"
		print(text)
		MAX_SYMBLOS = 2000
		text = text.prettify()[MAX_SYMBOLS*int(page):MAX_SYMBOLS+MAX_SYMBOLS*int(page)]

		to_replace = {
			"emphasis": "i",
			"title": "h2",
			"empty-line": "br",
			"section": "div class=\"book-section\""
		}
		for i in to_replace:
			print(i, "=", to_replace[i])
			text = text.replace(tag(i), tag(to_replace[i]))
			text = text.replace(ctag(i), ctag(to_replace[i]))

	data = {"book": book, "book_text": text, "section_title": section_title}
	RENDER = render(request, "riddles/books_index.html", context=data)
	return RENDER
