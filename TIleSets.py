## uploading tilesets to the database
tilesets upload-source miffll populated-places-source populated_places.geojson.ld

## deleteing tilesets
tilesets delete-source miffll PumphousePark

##creating tilesets
tilesets create miffll.missing-links --recipe missing-links.json --name "missing links"

## updating tileset recipes
 tilesets update-recipe miffll.missing-links missing-links.json
 
 ## publish tilesets
 tilesets publish miffll.missing-links


tilesets create miffll.missing-links --recipe missing-links.json --name "missing links" --token sk.eyJ1IjoibWlmZmxsIiwiYSI6ImNsMW5tNXQ2MzB2dDkzaW9iazh6dGVtbmEifQ.j8ONnlDXTT8sNv8C2U-kXA

tilesets upload-source miffll BowRiver-Inglewood BowRiverInglewoodCon.geojson --token sk.eyJ1IjoibWlmZmxsIiwiYSI6ImNsMW5tNXQ2MzB2dDkzaW9iazh6dGVtbmEifQ.j8ONnlDXTT8sNv8C2U-kXA

tilesets upload-source miffll BowRiverCycleBridges BowRiverCycleBridges.geojson --token sk.eyJ1IjoibWlmZmxsIiwiYSI6ImNsMW5tNXQ2MzB2dDkzaW9iazh6dGVtbmEifQ.j8ONnlDXTT8sNv8C2U-kXA