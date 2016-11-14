               

$('#addMap').on('click', function addTerminalMapping () {
    // Создаем геообъект с типом геометрии "Точка".
        myGeoObject = new ymaps.GeoObject({
            // Описание геометрии.
           geometry: {
                type: "Point",
                coordinates: [55.81, 37.81]
            }
        });

    myMap.geoObjects
        .add(myGeoObject)        

}


)