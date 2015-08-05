Scenario: User login state user not logged in
	Given an open app
	When the user clicks the sell option
	And he is not logged in
	Then the sell screen will show the login/signup popup

Scenario: Initial seller screen
	Given an open SwipeBuy app
	And the user is logged in
	When the user clicks the sell option
	Then the camera feed screen will appear

Scenario: Camera feed screen
	Given a logged in user 
	When the user enters the camera feed
	Then a square camera feed will appear
	And a "Snap" button will appear

Scenario: Making a picture
	Given an open camera feed
	When the user clicks on "Snap"
	Then a square picture will be taken by the camera
	And the picture will be shown in the upload image gallery
	
Scenario: Upload image gallery
	Given a taken picture
	When the picture is generated
	Then it appears in the upload image gallery
	And a discard button will be shown at the top right corner of the picture
	And "Add more" button will be shown
	And "Next" button will be shown
	And all previously taken pictures will be shown next to "Add more" in chronological order (oldest leftmost)

Scenario: Upload image gallery with many pictures
	Given an open upload image gallery
	When the thumbnails doesn't fit the screen anymore
	Then there's a scrollbar below them

Scenario: Discarding current photo
	Given an open upload image gallery
	When the user clicks the discard button on the top right corner of the currently taken photo
	Then the image will be discraded
	And the user is taken back to the camera feed screen

Scenario: Add more photos
	Given an open upload image gallery
	When the user clicks "Add more"
	Then the user is taken back to the camera feed screen

Scenario: Discarding thumbnails
	Given an open upload image gallery
	When the user clicks the discard button on one of the thumbnails
	Then that photo is removed from the thumbnail roll

Scenario: Item description screen
	Given an open item description screen
	When the user enters the page
	Then the "price" is shown as an input field
	And the "currency" is shown as static text
	And the "description" is shown as text area
	And the "delivery - pickup option" is shown as an option box
	And the "delivery - delivery available option" is shown as an option box
	And the "thumbnail roll" is shown below them with a main image selected
	And the "post" button is shown

Scenario: Select a main photo
	Given an open item description screen
	And a default preselected main image
	When the user clicks a different image on the thumbnail roll
	Then that image becomes the main image

Scenario: Posting an item without description OR price
	Given an open item description screen
	When the user clicks the "post" button
	And the inputs are not valid
	Then the an error message is shown below that field

Scenario: Posting an item
	Given an open item description screen
	When the user clicks the "post" button
	And all the inputs are valid
	Then the "ready/share" screen is shown
	And the images are uploaded
	And the item is created in the backend

Scenario: Ready/share screen
	Given a ready/share screen
	When the user enters the screen
	Then a final message is shown on the screen
	And a "share" button is shown
	And an "OK" button is shown

Scenario: Sharing an item
	Given a ready/share screen
	When the user clicks the "share" button
	Then the native share feature pops up

Scenario: Ready/share OK
	Given a ready/share screen
	When the user clicks the "OK" button
	Then the user is taken to the dashboard
 