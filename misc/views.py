
from django.shortcuts import render, HttpResponse
import requests
import json
from ebird.api import region_observations, region_species, region_notable
from ebird.api import location_observations, location_species, location_notable
from ebird.api import hotspot_observations, hotspot_species, hotspot_notable

# Create your views here.

def index(request):
	return HttpResponse('Hello World!')


# def profile(request):
# 	parsedData = []
# 	if request.method == 'POST':
# 		username = request.POST.get('user')
# 		req = requests.get('https://api.github.com/users/' + username)
# 		jsonList = []
# 		jsonList.append(json.loads(req.content))
# 		userData = {}
# 		for data in jsonList:
# 			userData['name'] = data['name']
# 			userData['blog'] = data['blog']
# 			userData['email'] = data['email']
# 			userData['public_gists'] = data['public_gists']
# 			userData['public_repos'] = data['public_repos']
# 			userData['avatar_url'] = data['avatar_url']
# 			userData['followers'] = data['followers']
# 			userData['following'] = data['following']
# 			parsedData.append(userData)
# 		return render(request, 'misc/profile.html', {'data': parsedData})


# def profile(request):
#     if request.method == 'POST':

#         req = requests.get('http://api.wunderground.com/api/2581feba35497f37/tide/q/CA/San_Francisco.json')






def profile(request):
	obsList = {}
	if request.method == 'POST':
		region = request.POST.get('user')
		obsList = region_species('Neochmia modesta', 'AU')
		#obsList = region_observations(region, back=1)
	return render(request, 'misc/profile.html', {'data': obsList})

