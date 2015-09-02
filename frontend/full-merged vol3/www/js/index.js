var app = {
    temp : {
        DEVICE_WIDTH: window.innerWidth,
    },
    // Application Constructor
//    initialize: function() {
//        this.bindEvents();
//    },
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    geoEvents: function() {
        //Geoloc
        var self = this;

        $('#disabled #settings #do-check').on("click", self.checkState);
        var options = { timeout: 10000, enableHighAccuracy: true, maximumAge: 0 };
        navigator.geolocation.getCurrentPosition(self.onSuccess, self.onError, options);
        setTimeout(self.checkState, 500);
    },

    cameraEvents: function() {
    
        var self = this;
        
        document.getElementById('takePictureButton').addEventListener('mousedown', self.onTakePicture, false);
        document.addEventListener('deviceready', self.onDeviceReady, false);
    },

    //Geolocation
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
        console.log("Checking state...");
        $('#state li').removeClass('on off');

        cordova.plugins.diagnostic.isLocationEnabled(function(enabled){
            $('#state .location').addClass(enabled ? 'on' : 'off');
        }, self.onError);

        cordova.plugins.diagnostic.isLocationEnabled(
            function(e){
                if( e ) {
                    //console.log('Location Enabled');
                    $('#page1 #home').show();
                    $('ons-toolbar.navigation-bar').show();
                    $('#page1 #disabled').hide();
                }
                else {
                    //console.log('Location Disabled');
                    $('#page1 #disabled').show();
                    $('ons-toolbar.navigation-bar').hide();
                    $('#page1 #home').hide();
                     }           
            },

            function(e){
                console.log('Error '+e);
            }
        );

    },

/*
    onError: function(error){
        //console.error("An error occurred: "+error);
        alert('code: '    + error.code    + '\n' +
              'message: ' + error.message + '\n');
    },
*/


    //Camera
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

ons.bootstrap();

$(function(){
    setTimeout(function() {
        app.geoEvents();
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

setCamBackground = function() {
    $('ons-sliding-menu').children().css('background-color', 'transparent');
};

setCarouselHeight = function() {
    var stuff_height = $('ons-carousel-item .stuff').height();
    var buttons_height = $('ons-carousel-item .actions').height();
    var delivery_height = $('ons-carousel-item #delivery').height();
    // var comment_height = $('ons-carousel-item .comment').height() + 15;
    // var comment_num = $('ons-carousel-item .messages').find('.comment').length;
    // var text_height = $('ons-carousel-item .comment_textarea').height();
    var messages_height = $('ons-carousel-item .messages').height();
    $('ons-carousel').css('height', stuff_height + buttons_height + delivery_height + messages_height + 50);
};

/*
$(document).on("pageinit", '#page1', function() {
    $('#load_modal').show();
    setTimeout("$('#load_modal').hide()", 2000);

});
*/

//for swipeable image-modal!

/*
var images2 = ['img/1.jpg', 'img/2.jpg', 'img/3.jpg', 'img/4.jpg'];

createCarousel = function(imgs) {
    for (var i = 0; i < imgs.length; i++) {
        var imageURL = imgs[i];
        $("ons-modal#pic_modal ons-carousel").append('<ons-carousel-item><img src=' + imageURL + '></ons-carousel-item>');
        
    }
    
};
*/


$(document).on("pageinit", '#page1', function() {
    setCarouselHeight();

//    createCarousel(images2);  
    $("ons-carousel-item img", this).click(function() {
        $('#pic_modal').show();

        $('#close').click(function() {
            $('#pic_modal').hide();
        });

//        carousel.refresh();        
  });
    
});



$(document).on('picture-ready', function() {
    app.initSlide();
});

$(document).on('pageinit', '#camera', function() {
    setCamBackground();
    app.cameraEvents();
    app.onStartCamera();
});

$(document).on('pageinit', '#description', function() {
    app.initDescription();
});









