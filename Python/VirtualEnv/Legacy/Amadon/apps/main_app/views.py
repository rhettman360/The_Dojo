from __future__ import unicode_literals
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect

productInfo = {
"products" : {
"item_id" : [1,2,3,4,5,],
"name" : ["10 Arrows", "5 Deku Nuts", "30 Deku Seeds", "Deku Shield", "Deku Stick"],
"price" : [20, 15, 30, 40, 10],
},
}

def index(request):
    global productInfo
    dataSubmit = {'code':""}
    print
    for items in range(0,len(productInfo['products']['item_id'])):
        itemname = "item"+str(items)
        itemprice = "price"+str(items)
        csrf_string = get_token(request)
        dataSubmit["code"] += "<form action='/results' method='post'><input type='hidden' name='csrfmiddlewaretoken' value='{}'><input type='hidden' name='product_id' value='{}'><div class='row'><cart>".format(csrf_string, productInfo['products']['item_id'][items])+ str(str(productInfo['products']['name'][items]) + " for " +str(productInfo['products']['price'][items])+ " rupies " +"<div class='input-field col l1 offset-0'><select name= 'quantity' class='icons'><option value='' disabled selected><option name= 'quantity' value='1'>1</option><option name= 'quantity' value='2'>2</option><option name= 'quantity' value='3'>3</option><option name= 'quantity' value='4'>4</option><option name= 'quantity' value='5'>5</option></select><label>Quantity</label></div><input class='waves-effect waves-light btn' type='submit' value='checkout'></form></div>")
    if "total" not in request.session.keys():
        request.session['total'] = 0
    if "current" not in request.session.keys():
        request.session['current'] = 0
    if "items" not in request.session.keys():
        request.session['items'] = 0
    return render(request, "main_app/index.html", dataSubmit)

def submitter(request):
    # print request.POST['product_id']
    # print request.POST['quantity']
    total = int(productInfo['products']['price'][int(request.POST['product_id'])-1])*int(request.POST['quantity'])
    request.session['total'] += total
    request.session['items'] += int(request.POST['quantity'])
    request.session['current'] = total
    # print request.session['total']
    return redirect("/checkout")

def checkout(request):
    return render(request, "main_app/checkout.html")

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    if "total" not in request.session.keys():
        request.session['total'] = 0
    if "current" not in request.session.keys():
        request.session['current'] = 0
    if "items" not in request.session.keys():
        request.session['items'] = 0
    global productInfo
    dataSubmit = {'code':""}
    print
    for items in range(0,len(productInfo['products']['item_id'])):
        itemname = "item"+str(items)
        itemprice = "price"+str(items)
        csrf_string = get_token(request)
        dataSubmit["code"] += "<form action='/results' method='post'><input type='hidden' name='csrfmiddlewaretoken' value='{}'><input type='hidden' name='product_id' value='{}'><div class='row'><cart>".format(csrf_string, productInfo['products']['item_id'][items])+ str(str(productInfo['products']['name'][items]) + " for " +str(productInfo['products']['price'][items])+ " rupies " +"<div class='input-field col l1 offset-0'><select name= 'quantity' class='icons'><option value='' disabled selected><option name= 'quantity' value='1'>1</option><option name= 'quantity' value='2'>2</option><option name= 'quantity' value='3'>3</option><option name= 'quantity' value='4'>4</option><option name= 'quantity' value='5'>5</option></select><label>Quantity</label></div><input class='waves-effect waves-light btn' type='submit' value='checkout'></form></div>")
    if "total" not in request.session.keys():
        request.session['total'] = 0
    if "current" not in request.session.keys():
        request.session['current'] = 0
    if "items" not in request.session.keys():
        request.session['items'] = 0
    return render(request, "main_app/index.html", dataSubmit)
