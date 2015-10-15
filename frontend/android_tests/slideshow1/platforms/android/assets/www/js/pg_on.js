var images
//import images somehow
//images is an array


createImageItem = function(images) {
	for (i=0; i<images.length; i++) {
		imageURL = images[i];
		$("body ul.pgwSlideshow").append('<li><img src=imageURL></li>');
	}
}

//var HTMLpictureItem = '<li><img src=imageURL></li>'
//$("body ul").append(HTMLpictureItem);



