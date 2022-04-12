// map.on('load', () => {
    //     map.addSource('park-pathways', {
    //         type: 'vector',
    //         url: 'mapbox://miffll.park-pathways'
    //     });
    //     map.addLayer({
    //         'id': 'GreenwayNorth',
    //         'type': 'line',
    //         'source': 'park-pathways',
    //         'source-layer': 'GreenwayNorth',
    //         'layout': {
    //             'line-join': 'round',
    //             'line-cap': 'round'
    //         },
    //         'paint': {
    //             'line-color': 'rgb(0, 255, 0)',
    //             'line-width': 10
    //         }
    //     });
        
    //  map.on('click', (e) => {

    //     const bbox = [
    //         [e.point.x - 6, e.point.y - 6],
    //         [e.point.x + 6, e.point.y + 6]
    //     ];

    //     setFeature(map.queryRenderedFeatures(bbox, { layers: ['park-pathways'] }));
    //     console.log(feature);
    // });

    // });


    const [feature, setFeature] = useState(null);