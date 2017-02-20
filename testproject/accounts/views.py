from django.shortcuts import render,HttpResponse
from accounts.models import Dreamreal
from django.http import HttpResponse

#def home(request):
    #return HttpResponse('<p> Home Page </p>')
 #   return render(request,'accounts/login.html')
# Create your views here.




def crudops(request):
    # Creating an entry

    dreamreal = Dreamreal(
        website="www.polo.com", mail="sorex@polo.com",
        name="sorex", phonenumber="002376970"
    )

    dreamreal.save()

    # Read ALL entries
    objects = Dreamreal.objects.all()
    res = 'Printing all Dreamreal entries in the DB : <br>'

    for elt in objects:
        res += elt.name + "<br>"

    # Read a specific entry:
    sorex = Dreamreal.objects.get(name="sorex")
    res += 'Printing One entry <br>'
    res += sorex.name

    # Delete an entry
    res += '<br> Deleting an entry <br>'
    sorex.delete()

    # Update
    dreamreal = Dreamreal(
        website="www.polo.com", mail="sorex@polo.com",
        name="sorex", phonenumber="002376970"
    )

    dreamreal.save()
    res += 'Updating entry<br>'

    dreamreal = Dreamreal.objects.get(name='sorex')
    dreamreal.name = 'thierry'
    dreamreal.save()

    return HttpResponse(res)
    #return render(request, 'accounts/login.html')

def CreateData(request):
    dreamreal = Dreamreal(
        website="www.polo.com", mail="sorex@polo.com",
        name="sorex", phonenumber="002376970"
    )
    dreamreal.save()
    res = 'Create Dreamreal entries in the DB successful <br>'
    return HttpResponse(res)

def GetData(request):
    objects = Dreamreal.objects.all()
    res = 'Printing all Dreamreal entries in the DB : <br>'

    for elt in objects:
        res += elt.name + "<br>"

    # Read a specific entry:
    #sorex = Dreamreal.objects.get(name="akash")
    #res += 'Printing One entry <br>'
    #res += sorex.name
    return HttpResponse(res)

def UpdateData(request):
    dreamreal = Dreamreal(
        website="www.polo.com", mail="sorex@polo.com",
        name="sorex", phonenumber="002376970"
    )

    dreamreal.save()

    res = 'Updating entry<br>'

    dreamreal = Dreamreal.objects.get(name='sorex')
    dreamreal.name = 'thierry'
    dreamreal.save()
    res += 'Update successful<br>'
    return HttpResponse(res)
def DeleteData(request):
    res = '<br> Deleting an entry <br>'
    sorex.delete()
    res += 'Delete successful<br>'
    return HttpResponse(res)

