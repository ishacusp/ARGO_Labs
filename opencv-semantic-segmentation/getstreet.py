#My plan is to put this chunk of code into a function instead to make it reproducible for different locations 
import google_streetview.api

# Define parameters for street view api
params = [{
  'size': '600x300', # max 640x640 pixels
  'location': '2nd Ave & E 1st St, New York, NY 10003',
  'heading': '270',
  'pitch': '-0.76',
  'fov': '180',
  'key': 'XXXXX
}]

# Create a results object
results = google_streetview.api.results(params)

# Download images to directory 'images'
results.download_links('opencv-semantic-segmentation/images/')