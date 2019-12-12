from django.shortcuts import render


# Create your views here.
def all_transfers(request):
    text_views = "to jest tekst z views"
    transfery = ['123', '9999', '516']
    return render(request, 'transfer_list.html',
                  {'text': text_views, 'transfery': transfery, 'moze_ogladac': True})
