import json
import gpxpy
import gpxpy.gpx

# Loeb sisse Elroni lehelt saadud peatuste JSON'i
sisfail = input('JSON faili asukoht: ')
with open(sisfail, 'r') as file:
    sisjson = json.loads(file.read())['data']
    

# Võtab JSON'i ja paneb selle gpx objekti
valgpx = gpxpy.gpx.GPX()
for entry in sisjson:
    peatus = gpxpy.gpx.GPXWaypoint()
    peatus.name = entry['peatus']
    peatus.latitude = entry['latitude']
    peatus.longitude = entry['longitude']
    valgpx.waypoints.append(peatus)
    
# Kirjutab faili
    
with open('val.gpx', 'w') as file:
    file.write(valgpx.to_xml())
