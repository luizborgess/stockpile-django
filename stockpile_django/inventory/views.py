from django.shortcuts import render, redirect,get_object_or_404
from .models import Item
from .forms import ItemForm


def index(request):
    items = Item.objects.all()
    return render(request, "index.html", {"items": items})

def new_item(request):
    form = ItemForm()
    return render(request, "form.html", {"form": form})

def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return redirect("/item/new")

def add_qty(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.qty += 1
    item.save()
    return redirect("/")

def remove_qty(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if item.qty > 0:
        item.qty -= 1
        item.save()
    return redirect("/")