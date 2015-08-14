var app = {
    temp : {
        DEVICE_WIDTH: window.innerWidth,
    },
    // Application Constructor
    initialize: function() {
        this.bindEvents();
    },
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
        document.getElementById('startCameraButton').addEventListener('mousedown', this.onStartCamera, false);
        document.getElementById('startCameraAnotherPosButton').addEventListener('mousedown', this.onStartCameraAnotherPos, false);

        document.getElementById('stopCameraButton').addEventListener('mousedown', this.onStopCamera, false);
        document.getElementById('takePictureButton').addEventListener('mousedown', this.onTakePicture, false);
        document.getElementById('switchCameraButton').addEventListener('mousedown', this.onSwitchCamera, false);
        // document.getElementById('showButton').addEventListener('mousedown', this.onShow, false);
        // document.getElementById('hideButton').addEventListener('mousedown', this.onHide, false);
        // document.getElementById('colorEffectCombo').addEventListener('change', this.onColorEffectChanged, false);
        //window.addEventListener('orientationchange', this.onStopCamera, false);
        document.addEventListener('deviceready', this.onDeviceReady, false);
    },

    onStartCamera: function() {
        var tapEnabled = true;
        var dragEnabled = true;
        var toBack = true;
        cordova.plugins.camerapreview.startCamera({x: 0, y: 0, width: app.temp.DEVICE_WIDTH, height: app.temp.DEVICE_WIDTH}, "back", tapEnabled, dragEnabled, toBack);
    },
    onStartCameraAnotherPos: function() {
        var tapEnabled = true;
        var dragEnabled = true;
        var toBack = false;
        cordova.plugins.camerapreview.startCamera({x: 0, y: 0, width: app.temp.DEVICE_WIDTH, height: app.temp.DEVICE_WIDTH}, "front", tapEnabled, dragEnabled, toBack);
    },
    onStopCamera: function() {
        cordova.plugins.camerapreview.stopCamera();
    },
    onTakePicture: function() {
        cordova.plugins.camerapreview.takePicture({maxWidth:640, maxHeight:640});
    },
    onSwitchCamera: function() {
        cordova.plugins.camerapreview.switchCamera();
    },
    // onShow: function() {
    //  cordova.plugins.camerapreview.show();
    // },
 //    onHide: function() {
 //        cordova.plugins.camerapreview.hide();
 //    },
    // onColorEffectChanged: function() {
    //  var effect = document.getElementById('colorEffectCombo').value;
    //  cordova.plugins.camerapreview.setColorEffect(effect);
    // },

    // deviceready Event Handler
    onDeviceReady: function() {
        //on picture
        cordova.plugins.camerapreview.setOnPictureTakenHandler(function(result){
            document.getElementById('originalPicture').src = result[0];//originalPicturePath;
            document.getElementById('previewPicture').src = result[1];//previewPicturePath;
            appendImage(result[1]);
        });
    //     app.receivedEvent('deviceready');
    // },

    // receivedEvent: function(id) {
    //     var parentElement = document.getElementById(id);
    //     var listeningElement = parentElement.querySelector('.listening');
    //     var receivedElement = parentElement.querySelector('.received');

    //     listeningElement.setAttribute('style', 'display:none;');
    //     receivedElement.setAttribute('style', 'display:block;');

    //     console.log('Received Event: ' + id);
    // }
    },
};
app.initialize();

var images = [];
function appendImage(result) {
    images.push(result);
};






