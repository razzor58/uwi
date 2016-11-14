var myMap;

// Дождёмся загрузки API и готовности DOM.
ymaps.ready(init);

function init () {
    // Создание экземпляра карты и его привязка к контейнеру с
    // заданным id ("map").
    myMap = new ymaps.Map('map', {
        // При инициализации карты обязательно нужно указать
        // её центр и коэффициент масштабирования.
        center:[55.76, 37.64], // Москва
        zoom:10
    });

}                      

function addPoint(x,y) {

	    // Создаем геообъект с типом геометрии "Точка".
        myGeoObject = new ymaps.GeoObject({
            // Описание геометрии.
           geometry: {
                type: "Point",
                coordinates: [x, y]
//                coordinates: [55.8, 37.8]
            }
        });

        // Для уничтожения используется метод destroy.
	myMap.geoObjects.add(myGeoObject)        
    };


