$(window).load(function(){

// var images = ["img/1.jpg", "img/2.jpg", "img/3.jpg", "img/4.jpg", "img/5.jpg", "img/6.jpg"];

    createImageItem = function(imgs) {
        for (i=0; i<imgs.length; i++) {
            var imageURL = imgs[i];
            $("ul").append('<li><img src=' + imageURL + '></li>');
            //<input type="image" src="img/del2.png" />
        }
    }
    createImageItem(images);


    $('.pgwSlideshow').pgwSlideshow();

    $('.pgwSlideshow .ps-current li').append('<input type="image" src="img/del2.png" />');
    $(".pgwSlideshow .ps-current li input").click(function(){
        $(this).parents("li").remove();
        $('.pgwSlideshow .ps-list li .ps-item.ps-selected').remove();
        $(".pgwSlideshow .ps-current li img").next().show();
    });

});
