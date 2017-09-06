my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dickin(a):
    newarr = []
    for element in a:
        tup = ("")
        tup = tup + element, a[element]
        newarr.append(tup)
    return newarr

print dickin(my_dict)
#end
