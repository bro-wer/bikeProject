var selectedStations = [];
var stationsToMarkersMap = {};

var mapOptions = {};
var map = "";

function filterStationsList() {
    // Declare variables
    var input, filter, ul, li, a, i;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function toggleStationMarker(stationId, coordinates) {
  if (selectedStations.indexOf(stationId) >= 0) {
    var newMarker = stationsToMarkersMap[stationId];
    newMarker.setMap(null);
    selectedStations.pop(stationId);

    var e = document.getElementById(stationId).style.color = "red";
    console.log("e");
    console.log(e);


  } else {
    selectedStations.push(stationId);
    var newMarker = addMarker(coordinates[1], coordinates[0]);
    stationsToMarkersMap[stationId] = newMarker;
  }
}



function myMap() {
    mapOptions = {
      center: new google.maps.LatLng(52.4028313, 16.9116229),
      zoom: 12,
      mapTypeId: google.maps.MapTypeId.HYBRID
    }
    map = new google.maps.Map(document.getElementById("map"), mapOptions);
  }


  function addMarker (lattitude, longitude) {
    var position = {lat: lattitude, lng: longitude};
    var marker = new google.maps.Marker({position: position, map: map}, mapOptions);
    return marker;
  }
