from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Apple","limit":2,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images


gimages -k AIzaSyDI6T5Ir5qmeCVBvODgXMmpng67rtWMCsY -c '010078415391490852567:8bsnckg5cpc' search -q 'donald trump' -d ./trump --num 10
