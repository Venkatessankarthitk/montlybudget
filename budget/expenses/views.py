import json
import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from expenses.models import purchasing_items, expenses_details 
from django.core import serializers
from django.views.generic.base import TemplateView 
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.decorators import api_view
from rest_framework.decorators import list_route, detail_route

class ExpensesPage(TemplateView):
	template_name = "expenses.html"


#def index(request):
	#return HttpResponse("Hello, world. You're in budget expenses page index.")

#	return render(request, 'expenses.html')

def purchase_item(request):
	purchase =json.dumps(list(purchasing_items.objects.values()))
	return HttpResponse(purchase, content_type='application/json')

@list_route(methods=["GET","POST" ])
def abcd(request):
	try:
		parchesed_details = dict(item.split("=") for item in (request.META['QUERY_STRING']).split("&"))
		parchesed_data = expenses_details( parchased_product= parchesed_details['purchase_items'] ,
			parchased_price= parchesed_details['price'], parchased_date= parchesed_details['date'] )
		parchesed_data.save()
		return HttpResponse("Sucessfully Added the purchased details")
	except Exception:
		return HttpResponse("Error in Adding the purchased details")

def expenses(request):
	purchase =(expenses_details.objects.all().values())
	list_result = [entry for entry in purchase]
	response = json.dumps(list_result, cls=DjangoJSONEncoder) 
	return  HttpResponse(response)

class dashboard(TemplateView):
	template_name = "dashboard.html"




	
