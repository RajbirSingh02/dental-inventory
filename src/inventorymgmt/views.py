from django.shortcuts import render, redirect
from .models import *
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm, IssueForm, ReorderLevelForm
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
		"title": title,
	}
	return redirect('/items')
	#return render(request, "home.html",context)

@login_required
def items(request):
	header = 'List of items'
	form = StockSearchForm(request.POST or None)
	queryset = Stock.objects.all()
	context = {
		"header": header,
		"queryset": queryset,
		"form": form,
	}
	if request.method == 'POST':
		queryset = Stock.objects.filter(category__icontains=form['category'].value(),
									#item_name__icontains=form['item_name'].value()
									)

		if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
			writer = csv.writer(response)
			writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
			instance = queryset
			for stock in instance:
				writer.writerow([stock.category, stock.item_name, stock.quantity])
			return response

		context = {
		"form": form,
		"header": header,
		"queryset": queryset,
	}

	return render(request, "items.html",context)

@login_required
def add_items(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/items')
	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "add_items.html", context)

def update_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully Saved')
			return redirect('/items')

	context = {
		'form':form
	}
	return render(request, 'add_items.html', context)

def delete_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Deleted Successfully ')
		return redirect('/items')
	return render(request, 'delete_items.html')

def stock_detail(request, pk):
	queryset = Stock.objects.get(id=pk)
	context = {
		"title": queryset.item_name,
		"queryset": queryset,
	}
	return render(request, "stock_detail.html", context)

def issue_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance =  form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		messages.success(request, "Issued Sucessfully. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
		instance.save()
		return redirect('/stock_detail/'+str(instance.id))

	context = {
		"title": 'Issue ' + str(queryset.item_name),
		"queryset": queryset,
		"form": form,
		"username": 'Issue By: ' + str(request.user),
	}

	return render(request, "add_items.html", context)


def reorder_level(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReorderLevelForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Reorder level for " + str(instance.item_name) + " is updated to " + str(instance.reorder_level))

		return redirect("/items")
	context = {
			"instance": queryset,
			"form": form,
		}
	return render(request, "add_items.html", context)
