var app = {

    // Application Constructor
    initialize: function() {
        
        //$('body').addClass(device.platform.toLowerCase());
        // Bind events
//        $(document).on("resume", this.onResume);
        var self = this;

        $('#settings #do-check').on("click", self.checkState);
//        $('#settings #location-settings').on("click", function(){
//        diagnostic.switchToLocationSettings();
//        });
        var options = { timeout: 10000, enableHighAccuracy: true, maximumAge: 0 };
        navigator.geolocation.getCurrentPosition(self.onSuccess, self.onError, options);

        setTimeout(self.checkState, 500);
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
   
    checkState: function(){
        var self = this;
        console.log("Checking state...");
        $('#state li').removeClass('on off');

        cordova.plugins.diagnostic.isLocationEnabled(function(enabled){
            $('#state .location').addClass(enabled ? 'on' : 'off');
        }, self.onError);
    },

    onError: function(error){
        //console.error("An error occurred: "+error);
        alert('code: '    + error.code    + '\n' +
              'message: ' + error.message + '\n');
    },

//   onResume: function(){
//       this.checkState();
//  }
};

app.initialize();
