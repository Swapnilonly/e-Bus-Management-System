from django.shortcuts import render, redirect

# from webapp.models import Usersignup
# from webapp.models import PostBusInfo
# from webapp.models import PostBusContact
from webapp.models import *


# Create your views here.
###########   BUS CONTACT   ###########
def BusContact(request):
    obj = PostBusContact.objects.all()
    return render(request,"BusContact.html",{'obj':obj})


###########   BUSINFO PAGE   ###########
def BusInfo(request):
    obj = PostBusInfo.objects.all()
    return render(request,"BusInfo.html",{'obj':obj})


###########   BUSTYPE PAGE   ###########
def BusType(request):
    obj = PostBusType.objects.all()
    return render(request,"BusType.html",{'obj':obj})

###########   HOME PAGE   ###########
def index(request):
    return render(request,"index.html")

###########   ABOUT PAGE   ###########
def about(request):
    return render(request, "about.html")

###########   CONTACT PAGE   ###########
def contact(request):
    return render(request,"contact.html")

###########   SERVICES PAGE   ###########
def services(request):
    return render(request,"services.html")

###########   LOGIN PAGE   ###########
def Login(request):
    msg = ""  # Initialize msg at the start

    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')

        # Admin login check
        if username == 'admin' and pwd == 'admin':
            return render(request, "Post_Bus_info.html")

        # User authentication
        user_exists = Usersignup.objects.filter(username=username, password=pwd).first()

        if user_exists:
            bustype = PostBusType.objects.all()
            return render(request, "bustype.html", {'bustype': bustype})

        # If login fails
        msg = "Incorrect username or password."

    # This return ensures a response is always sent
    return render(request, "Login.html", {'msg': msg})


###########   SIGNUP PAGE   ###########
def signup(request):
    msg=""
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        phnum = request.POST['phnum']
        address = request.POST['address']
        password = request.POST['pwds']

        # Check if email already exists
        if Usersignup.objects.filter(email=email).exists():
            msg = "Email ID already exists. Please use another email."
        else:
            obj = Usersignup(username=uname, email=email, phnum=phnum, address=address, password=password)
            obj.save()
            msg = "Signup Successfully"
    return render(request,"Login.html",{'msg':msg})


###########   FORGOT PASSWORD PAGE   ###########
def forgot_password(request):
    return render(request,"forgot_password.html")


###########   POST BUS INFO PAGE   ###########

def Post_Bus_info(request):
    msg = ""
    if request.method == "POST":
        print("Received POST data:", request.POST)
        busnumber = request.POST.get('busNumber')
        routename = request.POST.get('routeName')
        departuretime = request.POST.get('departureTime')
        arrivaltime = request.POST.get('arrivalTime')
        busfair = request.POST.get('busFare', None)  # Get busFare directly
        print(f"Captured Bus Fare: {busfair}")  # Debugging

        if busnumber and routename and departuretime and arrivaltime and busfair:
            obj = PostBusInfo(
                busnumber=busnumber,
                routename=routename,
                departuretime=departuretime,
                arrivaltime=arrivaltime,
                busfair=busfair
            )
            obj.save()
            msg = "Bus information posted successfully"
        else:
            msg = "All fields are required!"

    return render(request, "Post_Bus_info.html", {'msg': msg})
###########   POST BUS CONTACT PAGE   ###########
def Post_Contact(request):
    msg=""
    if(request.method=='POST'):
        contactperson = request.POST['contactPerson']
        contactemail = request.POST['contactEmail']
        contactphone = request.POST['contactPhone']
        contactaddress = request.POST['contactAddress']
        obj = PostBusContact(contactperson=contactperson,contactemail=contactemail,contactphone=contactphone,contactaddress=contactaddress)
        obj.save()
        msg="Bus contact posted successfully"
        return render(request,"Post_Contact.html",{'msg':msg})
    return render(request,"Post_Contact.html")

###########   POST BUS TYPE PAGE   ###########
def Post_Bus_type(request):
    msg = ""
    selected_option = ""
    if request.method == 'POST':
        option_id = request.POST['busType']
        buscapacity = request.POST['busCapacity']
        busdescription = request.POST['busDescription']
        obj = PostBusType(bustype=option_id,buscapacity=buscapacity,buscdescription=busdescription)
        obj.save()
        msg = "bus type posted successfully"
        return render(request,'Post_Bus_type.html',{'msg':msg})
    return render(request,"Post_Bus_type.html")

########### Admin view Bus Info  ############
def adminviewbusinfo(request):
    obj = PostBusInfo.objects.all()
    return render(request, "adminviewbusinfo.html", {'obj': obj})


########### Admin view Bus Contact  ############
def adminviewbuscontact(request):
    obj = PostBusContact.objects.all()
    return render(request, "adminviewcontact.html", {'obj': obj})


########### Admin view Bus Type  ############
def adminviewbustype(request):
    obj = PostBusType.objects.all()
    return render(request, "adminviewbustype.html", {'obj': obj})


########### Admin view Bus Type  ############
def adminviewuser(request):
    obj = Usersignup.objects.all()
    return render(request,"adminviewuser.html",{'obj':obj})

########### Bus Booking  ############
def bookyourbus(request):
    msg = ""
    if request.method == "POST":
        busNumber = request.POST['busnumber']
        traveldate = request.POST['travel_date']
        numseats = request.POST['num_seats']
        obj = Busbooking(busnumber= busNumber,travel_date=traveldate,numseats=numseats)
        obj.save()
        msg = "Welcome"
        Busnumber = PostBusInfo.objects.get(busnumber==busNumber)
        if(Busnumber):
            return render(request,'paynow.html')

    return render(request,"bookyourseat.html")

###########  For Payment  ############
def paynow(request):
    return render(request,'paynow.html')
