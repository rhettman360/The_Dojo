from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import random

def randomWord():
    vowel = ("u", "a", "ae", "e", "eh", "ur", "i", "ee", "o", "ah", "ou", "oo", "ow", "ei", "oy", "ai", "er", "ure")
    notVowel = ("b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ing", "p", "r", "s", "sh", "t", "ch", "th", "ge", "si", "z", "v", "w")
    word = ""
    for count in range(0, 7):
        word += str(random.choice(vowel)) + str(random.choice(notVowel))
        if len(word)>14:
            break
    return word[:14]

def clock(request):
    if request.method == "POST":
        if "counter" not in request.session.keys():
            request.session['counter'] = 0
        request.session['counter'] += 1
        context = {
        "word": randomWord(),
        }
        return render(request,'generator/index.html', context)
    else:
        context = {
        "word": "Make a random word!",
        }
        print context
        return render(request,'generator/index.html', context)
