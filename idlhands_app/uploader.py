def handle_uploaded_file(request):

    file_data = {'image': SimpleUploadedFile('.jpg', request.FILES)}
    pass
