$(document).ready(function(){
    var images = ["img/1.jpg", "img/2.jpg", "img/3.jpg", "img/4.jpg", "img/5.jpg", "img/6.jpg", "img/7.png", "img/8.jpg", "img/9.jpg"];


    createImage = function(imgs) {
        for (i = 0; i < imgs.length; i++) {
            var imageURL = imgs[i];
            $(".wrapper").append('<div class="pic"><img src=' + imageURL + '></div>');
        }
    };


    setWidth = function() {
        var img_num = $('.wrapper').children().length;
        var img_width = $('.wrapper').children().width();
        var roll_width = img_num * (img_width + 10) + 6;
        $('.wrapper').css('width', roll_width);
    };

    createImage(images);
    setWidth();

    $('.pic').click(function() {
        $('.pic').removeClass('active');
        $(this).addClass('active');
    });

});
