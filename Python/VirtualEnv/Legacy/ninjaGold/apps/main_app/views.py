from django.shortcuts import render
import random

def index(request):
    if "gold_amt" not in request.session.keys():
        request.session['gold_amt'] = 0
    if "historystring" not in request.session.keys():
        request.session['historystring'] = ""
    return render(request, "main_app/index.html")

def farm(request):
    chance = random.randrange(1, 10)
    gain = random.randrange(10, 20)
    if chance > 5:
        request.session['gold_amt'] += gain
        histAdd = str("<p>Gained " + str(gain) + " at the Farm.</p>")
    else:
        request.session['gold_amt'] -= gain
        histAdd = str("<p>Lost " + str(gain) + " at the Farm. The price is wrong bitch</p>")
    request.session['historystring'] += histAdd
    context = {
    "historystring": request.session['historystring'],
    }
    return render(request, "main_app/index.html", context)

def cave(request):
    chance = random.randrange(1, 10)
    gain = random.randrange(5, 10)
    if chance > 5:
        request.session['gold_amt'] += gain
        histAdd = str("<p>Gained " + str(gain) + " at the Cave.</p>")
    else:
        request.session['gold_amt'] -= gain
        histAdd = str("<p>Lost " + str(gain) + " at the Cave. The price is wrong bitch</p>")
    request.session['historystring'] += histAdd
    context = {
    "historystring": request.session['historystring'],
    }
    return render(request, "main_app/index.html", context)

def house(request):
    chance = random.randrange(1, 10)
    gain = random.randrange(2, 5)
    if chance > 5:
        request.session['gold_amt'] += gain
        histAdd = str("<p>Gained " + str(gain) + " at the House.</p>")
    else:
        request.session['gold_amt'] -= gain
        histAdd = str("<p>Lost " + str(gain) + " at the House. The price is wrong bitch</p>")
    request.session['historystring'] += histAdd
    context = {
    "historystring": request.session['historystring'],
    }
    return render(request, "main_app/index.html", context)

def casino(request):
    chance = random.randrange(1, 10)
    gain = random.randrange(0, 50)
    if chance > 5:
        request.session['gold_amt'] += gain
        histAdd = str("<p>Gained " + str(gain) + " at the Casino.</p>")
    else:
        request.session['gold_amt'] -= gain
        histAdd = str("<p>Lost " + str(gain) + " at the Casino. The price is wrong bitch</p>")
    request.session['historystring'] += histAdd
    context = {
    "historystring": request.session['historystring'],
    }
    return render(request, "main_app/index.html", context)

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    if "gold_amt" not in request.session.keys():
        request.session['gold_amt'] = 0
    if "historystring" not in request.session.keys():
        request.session['historystring'] = ""
    return render(request, "main_app/index.html")
