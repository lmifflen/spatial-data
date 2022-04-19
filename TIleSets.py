## uploading tilesets to the database
tilesets upload-source miffll VistaHeights-source ./ParkAndBike/VistaHeights.geojson

## deleteing tilesets
tilesets delete-source miffll PumphousePark

##creating tilesets
tilesets create miffll.ParkAndBike --recipe ./ParkAndBike/ParkandBike.json --name "Park and Bike"

## updating tileset recipes
 tilesets update-recipe miffll.missing-links missing-links.json
 
 ## publish tilesets
 tilesets publish miffll.ParkAndBike
 
 export MAPBOX_ACCESS_TOKEN=sk.eyJ1IjoibWlmZmxsIiwiYSI6ImNsMW5tNXQ2MzB2dDkzaW9iazh6dGVtbmEifQ.j8ONnlDXTT8sNv8C2U-kXA

tilesets update-recipe miffll.park-pathways ./ParkPathways/park-pathways.json 






















## view recipe
tilesets view-recipe miffll.missing-links

## check status of upload
tilesets status miffll.missing-links