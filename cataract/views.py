from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
from .settings import MEDIA_ROOT

################################## AZURE #################################

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time


subscription_key = "a6ff3126d73847a39552834f34e59119"
endpoint = "https://cataract-api.cognitiveservices.azure.com/"

def cat(request):
    message = 'Upload as many files as you want!'
    response = ['NU', 'LL']
    if request.method == 'POST':

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

        # elif request.POST.get('submittext'):
            file_link_local = MEDIA_ROOT+"/documents/"
            file_link_remote = "https://cataractstorage.blob.core.windows.net/cataract-container/"

            file_name = str(request.FILES['docfile'])

            local_image_path = os.path.join (file_link_local, file_name)
            #local_image = open(local_image_path, "rb")

            remote_image = file_link_remote+file_name
            response = azureAPI(remote_image)
            print(response)

        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm() 
    # documents = Document.objects.all()

    return render(request, 'index.html', {'response': response, 'form': form}) #'documents': documents, 'message': message


def azureAPI(local_image):

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    #description_results = computervision_client.describe_image(remote_image_url )

    description_results = computervision_client.describe_image_in_stream(local_image)

    print("Description of remote image: ")

    if (len(description_results.captions) == 0):
        print("No description detected.")
        return(["No description detected.", 0])
    else:
        for caption in description_results.captions:
            print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
        return([description_results.tags, description_results.captions])
    print()