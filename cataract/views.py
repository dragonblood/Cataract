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
    response = {'tag': ['0'], 'confidence': [0]}
    file_name = '#'
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
            local_image = open(local_image_path, "rb")

            # remote_image = file_link_remote+file_name
            response = azureAPI(local_image)
            print(response)

        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm() 
    # documents = Document.objects.all()

    return render(request, 'index.html', {'response': response, 'form': form, 'img_name':"documents/"+file_name})


def azureAPI(image_url):

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    #description_results = computervision_client.describe_image(image_url)



    description_results_tags = computervision_client.tag_image_in_stream(image_url)
    print(description_results_tags)

    # description_results_describe = computervision_client.describe_image_in_stream(image_url)
    # print(description_results_describe)

    # if (len(description_results_tags.captions) == 0):
    #     print("No description detected.")
    #     return(["No description detected.", 0])
    # else:
        # for caption in description_results_describe.captions:
        #     print(caption.text, caption.confidence * 100)
        # return([description_results_describe.tags, description_results_describe.captions])


    ten = 0
    entity = {'tag':[], 'confidence':[]}

    if (len(description_results_tags.tags) == 0):
        print("No tags detected.")
    else:
        for tag in description_results_tags.tags:
            print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
            ten += 1
            entity['tag'].append(tag.name)
            entity['confidence'].append(tag.confidence * 100)
            # if ten == 10:
            #     break

        return(entity)