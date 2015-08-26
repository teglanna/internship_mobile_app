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
        document.getElementById('takePictureButton').addEventListener('mousedown', self.onTakePicture, false);
        document.addEventListener('deviceready', self.onDeviceReady, false);
    },

    onStartCamera: function() {
        var tapEnabled = true;
        var dragEnabled = true;
        var toBack = true;
        cordova.plugins.camerapreview.startCamera({x: 0, y: 0, width: app.temp.DEVICE_WIDTH, height: app.temp.DEVICE_WIDTH}, "back", tapEnabled, dragEnabled, toBack);
    },

    onTakePicture: function() {
        cordova.plugins.camerapreview.takePicture({maxWidth:640, maxHeight:640});
    },

    onDeviceReady: function() {
        app.onStartCamera();
        cordova.plugins.camerapreview.setOnPictureTakenHandler(function(result){
            document.getElementById('originalPicture').src = result[0];//originalPicturePath;
            document.getElementById('previewPicture').src = result[1];//previewPicturePath;
            appendImage(result[1]);
            $(document).trigger('picture-ready');
        });
    },

    initSlide: function() {
        createImageSlide(images);

        $('.pgwSlideshow').pgwSlideshow();

        $('.pgwSlideshow .ps-current li').append('<input type="image" src="img/del2.png" />');
        $(".pgwSlideshow .ps-current li input").click(function(){
            $(this).parents("li").remove();
            $('.pgwSlideshow .ps-list li .ps-item.ps-selected').remove();
            $(".pgwSlideshow .ps-current li img").next().show();
        });
    },

    initDescription: function() {
        createImageDescription(images);
        setRollWidth();
        setPicActive();
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


createImageSlide = function(imgs) {
    for (var i = imgs.length - 1; i >=0; i--) {
        var imageURL = imgs[i];
        $("ul").append('<li><img src=' + imageURL + '></li>');
        //<input type="image" src="img/del2.png" />
    }
};


createImageDescription = function(imgs) {
    for (var i = imgs.length - 1; i >=0; i--) {
        var imageURL = imgs[i];
        $(".wrapper").append('<div class="pic"><img src=' + imageURL + '></div>');
    }
};


setRollWidth = function() {
    var img_num = $('.wrapper img').length;
    var img_width = $('.wrapper img').width() + 10;
    var roll_width = img_num * img_width + 6;
    $('.wrapper').css('width', roll_width);
};

setPicActive = function() {
    $('.pic').click(function() {
        $('.pic').removeClass('active');
        $(this).addClass('active');
    });
};

$(document).on('picture-ready', function() {
    app.initSlide();
});


$(document).on('pageinit', '#description', function() {
    app.initDescription();
});










