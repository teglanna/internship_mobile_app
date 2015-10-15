function onDeviceReady() {
    $('body').addClass(device.platform.toLowerCase());
    // Bind events
    $(document).on("resume", onResume);
    $('#do-check').on("click", checkState);

    $('#settings #location-settings').on("click", function(){
        cordova.plugins.diagnostic.switchToLocationSettings();
    });

    // Make dummy geolocation request to cause authorisation request
    var onSuccess = function(position) {
            alert('Latitude: '          + position.coords.latitude        + '\n' +
                  'Longitude: '         + position.coords.longitude       + '\n' +
                  'Altitude: '          + position.coords.altitude        + '\n' +
                  'Accuracy: '          + position.coords.accuracy        + '\n' +
                  'Altitude Accuracy: ' + position.coords.altitudeAccuracy+ '\n' +
                //  'Heading: '           + position.coords.heading           + '\n' +
                //  'Speed: '             + position.coords.speed             + '\n' +
                  'Timestamp: '         + position.timestamp              + '\n');
    };
/*    function onError(error) {
        alert('code: '    + error.code    + '\n' +
              'message: ' + error.message + '\n');
    }
*/
    var options = { timeout: 8000, enableHighAccuracy: true, maximumAge: 3000 };
    navigator.geolocation.getCurrentPosition(onSuccess, onError, options);

    setTimeout(checkState, 500);


    function checkState(){
        console.log("Checking state...");

        $('#state li').removeClass('on off');

        cordova.plugins.diagnostic.isLocationEnabled(function(enabled){
            $('#state .location').addClass(enabled ? 'on' : 'off');
        }, onError);
    }

    function onError(error){
        console.error("An error occurred: "+error);
    }

    function onResume(){
        checkState();
    }
    
}

$(document).on("deviceready", onDeviceReady);