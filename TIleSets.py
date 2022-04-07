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


