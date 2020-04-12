# libraries are imported
import os
import requests
# rendering the template using render
from django.shortcuts import render
# this will be used to get the path of the media folder from settings
from django.conf import settings
# for storing the file in the desired folder, FileSystemStorage is used  
from django.core.files.storage import FileSystemStorage
# this will handle MultiValueDictKeyError using try and except
from django.utils.datastructures import MultiValueDictKeyError
# using class from models.py
from . models import file_storage
from django.templatetags.static import static



	
def file_storage_to_db(request):
	file_path = os.path.join(settings.CONTENT_DIR, 'assets/img')

	if request.method == 'POST':
		try:
			myFile = request.FILES['myFile']
		except MultiValueDictKeyError:
			print("Error.......")
			myFile = "None"
		fs = FileSystemStorage(location=file_path)	
		filename = fs.save(myFile.name, myFile)
		file_url = fs.url(filename)
		file_information = file_storage()
		file_information.file_name = myFile.name
		file_information.file_url = file_url 
		file_information.save()
		
		context = {
					'filename': myFile.name, 
					'file_url': file_url
				  }

		image = '/'.join([file_path, context['filename']])
		pred = predict(image)

		for name in os.listdir(file_path):
			if name != 'favicon.png' and name != 'LibrusLogo.png' and name != context['filename']:
				p = "/".join([file_path,name])
				os.remove(p)
		res = pred['result']['tags']
		return render(request, 'Cataract.html', {'label':res, 'context':context['filename'] })
	else:
		return render(request, 'Cataract.html')		

def predict(name):
	api_key = 'acc_77ab554b8ab01cf'
	api_secret = '134439d363b2cad920b1c6bec288d7ae'
	image_url = 'https://cdn.clippingpath.in/wp-content/uploads/2017/11/low-res.jpg'

	response = requests.get('https://api.imagga.com/v2/tags?image_url=%s' % image_url, auth=(api_key, api_secret))
	result = response.json()
	return(result)