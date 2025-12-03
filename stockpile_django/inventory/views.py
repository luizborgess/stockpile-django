from django.shortcuts import render, redirect,get_object_or_404
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    items = Item.objects.all()
    return render(request, "index.html", {"items": items})
@login_required
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

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    return render(request, "delete_confirm.html", {"item": item})

def add_10(request, id):
    item = get_object_or_404(Item, pk=id)
    item.qty += 10
    item.save()
    return redirect('/')


def sub_10(request, id):
    item = get_object_or_404(Item, pk=id)
    # Lógica opcional: Impedir que fique negativo
    if item.qty >= 10:
        item.qty -= 10
    else:
        item.qty = 0  # ou deixe ficar negativo se preferir

    item.save()
    return redirect('/')