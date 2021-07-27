from django.shortcuts import render
from .models import uploadModel
from django.contrib import messages
# from import_export import resources
# from .resources import uploadResource
from tablib import Dataset

# Create your views here.
def upload_file(request):
    data = uploadModel.objects.all()
    if request.method == 'POST':
        dataset = Dataset()
        print(dataset)
        newResource = request.FILES['myfile']
        if not newResource.name.endswith('xlsx'):
            messages.info(request, "Wrong file format")
            return render(request, "upload.html")
        imported_data = dataset.load(newResource.read(), format='xlsx')
        for data in imported_data:
            value = uploadModel(
                data[0], 
                data[1],
                data[2],
                data[3],
                data[4],
            )
            value.save()
            print("File uploaded sucessfully!")
    return render(request, 'upload.html', {'upload_data': data})

