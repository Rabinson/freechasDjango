from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	### if request.method == "POST":
		#do stuff
		#your_name = request.POST['Your Name']
		#your_email = request.POST['Your Email']
		#subject = request.POST['Subject']
		#message = request.POST['Message']

		#Send email
		#send_mail(
			#your_name, #subject
			#your_email, #message
			#your_name, #from
			#['sam_rabinson@gmail.com'], #to
			#fail_silently=False,
			#)

		#return render(request, 'contact.html', {'Your Name': your_name})

	#else: ###
	#return the page 
	return render(request, 'contact.html', {})
	
	