var app = {

    // Application Constructor
    initialize: function() {
        this.bindEvents();
        
        //$('body').addClass(device.platform.toLowerCase());
        // Bind events
    //    $(document).on("resume", this.onResume);
        $('#do-check').on("click", this.checkState);

        $('#settings #location-settings').on("click", function(){
        diagnostic.switchToLocationSettings();
        });

        var options = { timeout: 8000, enableHighAccuracy: true, maximumAge: 3000 };
        navigator.geolocation.getCurrentPosition(this.onSuccess, this.onError, options);

        setTimeout(this.checkState, 500);
    },
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
    },
    // deviceready Event Handler
    //
    // The scope of 'this' is the event. In order to call the 'receivedEvent'
    // function, we must explicitly call 'app.receivedEvent(...);'
    onDeviceReady: function() {
        app.receivedEvent('deviceready');
    },
    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        /*
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');
        */
        console.log('Received Event: ' + id);
    },
    
    // Make dummy geolocation request to cause authorisation request
    onSuccess: function(position) {
            alert('Latitude: '          + position.coords.latitude        + '\n' +
                  'Longitude: '         + position.coords.longitude       + '\n' +
                  'Altitude: '          + position.coords.altitude        + '\n' +
                  'Accuracy: '          + position.coords.accuracy        + '\n' +
                  'Altitude Accuracy: ' + position.coords.altitudeAccuracy+ '\n' +
                //  'Heading: '           + position.coords.heading           + '\n' +
                //  'Speed: '             + position.coords.speed             + '\n' +
                  'Timestamp: '         + position.timestamp              + '\n');
    },
/*    function onError(error) {
        alert('code: '    + error.code    + '\n' +
              'message: ' + error.message + '\n');
    }
*/
    
    checkState: function(){
        console.log("Checking state...");

        $('#state li').removeClass('on off');

        cordova.plugins.diagnostic.isLocationEnabled(function(enabled){
            $('#state .location').addClass(enabled ? 'on' : 'off');
        }, this.onError);
    },

    onError: function(error){
        console.error("An error occurred: "+error);
    },

//    onResume: function(){
//        this.checkState();
//    }
};

app.initialize();
