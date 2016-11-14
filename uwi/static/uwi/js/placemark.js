var myMap;

// ������� �������� API � ���������� DOM.
ymaps.ready(init);

function init () {
    // �������� ���������� ����� � ��� �������� � ���������� �
    // �������� id ("map").
    myMap = new ymaps.Map('map', {
        // ��� ������������� ����� ����������� ����� �������
        // � ����� � ����������� ���������������.
        center:[55.76, 37.64], // ������
        zoom:10
    });

}                      

function addPoint(x,y) {

	    // ������� ��������� � ����� ��������� "�����".
        myGeoObject = new ymaps.GeoObject({
            // �������� ���������.
           geometry: {
                type: "Point",
                coordinates: [x, y]
//                coordinates: [55.8, 37.8]
            }
        });

        // ��� ����������� ������������ ����� destroy.
	myMap.geoObjects.add(myGeoObject)        
    };


