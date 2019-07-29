from django.shortcuts import render,redirect
from django.http import HttpResponse 

# def create_session(request):
#     request.session['name'] = 'username'
#     request.session['password'] = 'password123'
#     return HttpResponse("<h1>dataflair<br> the session is set</h1>")
# def access_session(request):
#     response = "<h1>Welcome to Sessions of dataflair</h1><br>"
#     if request.session.get('name'):
#         response += "Name : {0} <br>".format(request.session.get('name'))
#     if request.session.get('password'):
#         response += "Password : {0} <br>".format(request.session.get('password'))
#         return HttpResponse(response)
#     else:
#         return redirect('create/')

# def delete_session(request):
#     try:
#         del request.session['name']
#         del request.session['password']
#     except KeyError:
#         pass
#     return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")


# def pdf_view(request):
#     pdf = render_to_pdf('login.html')
#     return HttpResponse(pdf,content_type='application/pdf')

from django.http import HttpResponse
from django.views.generic import View
 
from django.template.loader import get_template
 
from .utils import render_to_pdf 
 
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        
        pdf = render_to_pdf('login/invoice.html')
         
        response =  HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline'
        return response