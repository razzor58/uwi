               

$('#addMap').on('click', function addTerminalMapping () {
    // ������� ��������� � ����� ��������� "�����".
        myGeoObject = new ymaps.GeoObject({
            // �������� ���������.
           geometry: {
                type: "Point",
                coordinates: [55.81, 37.81]
            }
        });

    myMap.geoObjects
        .add(myGeoObject)        

}


)