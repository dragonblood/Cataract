from django.shortcuts import render

from google.cloud import vision
import io
import argparse


def cataractImageUpload(request):
    path = "/home/vipul/Documents/Project/Project Cataract 2.0/cataract/desert_sunset_landscape-wide.jpg"
    #path = "desert_sunset_landscape-wide.jpg"
    label_dict = vision_api(path)
    print(label_dict)
    return render(request, 'index.html', label_dict)


def vision_api(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_label_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    ten = 0
    label_dict = {'discription': [], 'score': [], 'topicality': []}

    for label in labels:
        label_dict['discription'].append(label.description)
        label_dict['score'].append(label.score)
        label_dict['topicality'].append(label.topicality)
        ten += 1
        if ten == 10:
            break

    return label_dict

# if response.error.message:
#     raise Exception(
#         '{}\nFor more info on error messages, check: '
#         'https://cloud.google.com/apis/design/errors'.format(
#             response.error.message))
