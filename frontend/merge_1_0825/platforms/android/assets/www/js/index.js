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
        var self = this;
        document.getElementById('startCameraButton').addEventListener('mousedown', self.onStartCamera, false);
        document.getElementById('startCameraAnotherPosButton').addEventListener('mousedown', self.onStartCameraAnotherPos, false);

        document.getElementById('stopCameraButton').addEventListener('mousedown', self.onStopCamera, false);
        document.getElementById('takePictureButton').addEventListener('mousedown', self.onTakePicture, false);
        document.getElementById('switchCameraButton').addEventListener('mousedown', self.onSwitchCamera, false);
        // document.getElementById('showButton').addEventListener('mousedown', this.onShow, false);
        // document.getElementById('hideButton').addEventListener('mousedown', this.onHide, false);
        // document.getElementById('colorEffectCombo').addEventListener('change', this.onColorEffectChanged, false);
        //window.addEventListener('orientationchange', this.onStopCamera, false);
        document.addEventListener('deviceready', self.onDeviceReady, false);
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
    initSlide: function() {
        createImageItem(images);

        $('.pgwSlideshow').pgwSlideshow();

        $('.pgwSlideshow .ps-current li').append('<input type="image" src="img/del2.png" />');
        $(".pgwSlideshow .ps-current li input").click(function(){
            $(this).parents("li").remove();
            $('.pgwSlideshow .ps-list li .ps-item.ps-selected').remove();
            $(".pgwSlideshow .ps-current li img").next().show();
        });

    }

};

$(function(){
    setTimeout(function() {
        app.bindEvents();
    }, 0);
});


var images = [];
function appendImage(result) {
    images.push(result);
};


createImageItem = function(imgs) {
    for (i=0; i<imgs.length; i++) {
        var imageURL = imgs[i];
        $("ul").append('<li><img src=' + imageURL + '></li>');
        //<input type="image" src="img/del2.png" />
    }
};

$(document).on('pageinit', '#slide', function() {
  app.initSlide();
})








