from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .models import User
from datetime import datetime
from .models import TrainingData

def retrieve_data(request):
    query = request.GET.get("query", "")  # Get the search query from the request
    filtered_data = []  # Initialize empty data to handle no search initially

    if query:
        # Search for matching training data based on the input text
        filtered_data = TrainingData.objects.filter(input_text__icontains=query)

    # Pass filtered data and the query to the template
    return render(request, 'retrieve.html', {'training_data': filtered_data, 'query': query})


def train_ai(request):
    if request.method == "POST":
        input_text = request.POST.get("input_text")
        output_text = request.POST.get("output_text")

        # Save the training data to the database
        TrainingData.objects.create(input_text=input_text, output_text=output_text)

        # Render the same form again with a success message
        return render(request, 'train.html', {'message': 'Training data submitted successfully!'})

    # Render the empty form for GET requests
    return render(request, 'train.html')

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
    return render(request, "contact.html")  




def sign(request):
       if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password= request.POST.get('password')
        sign = User(name=name, email=email, password=password)
        sign.save()
        return render(request, 'home.html')   
       return render(request , 'sign.html')



def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        users = User.objects.filter(name=name, password=password)
        if users.exists():
            user = users.first()  # Get the first matching user
            return render(request, 'home.html', {'message': f'Welcome, {user.name}!'})
        else:
            return render(request, 'login.html', {'error': 'Invalid name or password!'})
    return render(request, 'login.html')



def ai(request):
    return render(request, 'ai.html')


