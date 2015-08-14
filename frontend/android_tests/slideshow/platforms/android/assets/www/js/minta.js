//Helper
/*
These are HTML strings
*/
var HTMLheaderName = '<h1 id="name">%data%</h1>';
var HTMLheaderRole = '<span>%data%</span><hr/>';

var HTMLcontactGeneric = '<li class="flex-item"><span class="orange-text">%contact%</span><span class="white-text">%data%</span></li>';
var HTMLmobile = '<li class="flex-item"><span class="orange-text">mobile</span><span class="white-text">%data%</span></li>';
var HTMLemail = '<br><li class="flex-item"><span class="orange-text">email</span><span class="white-text">%data%</span></li>';
var HTMLtwitter = '<li class="flex-item"><span class="orange-text">twitter</span><span class="white-text">%data%</span></li>';
var HTMLgithub = '<li class="flex-item"><span class="orange-text">github</span><span class="white-text">%data%</span></li>';
var HTMLblog = '<li class="flex-item"><span class="orange-text">blog</span><span class="white-text">%data%</span></li>';
var HTMLlocation = '<li class="flex-item"><span class="orange-text">location</span><span class="white-text">%data%</span></li>';

var HTMLbioPic = '<img src="%data%" class="biopic">';
var HTMLwelcomeMsg = '<span class="welcome-message">%data%</span>';

var HTMLskillsStart = '<h3 id="skillsH3">Skills at a Glance:</h3><ul id="skills" class="flex-box"></ul>';
var HTMLskills = '<li class="flex-item"><span class="white-text">%data%</span></li>';

var HTMLworkStart = '<div class="work-entry"></div>';
var HTMLworkEmployer = '<h3>%data%</h3>'; //<a href="#">rendszer
var HTMLworkTitle = '<div class = "content">%data%</div>'; // - %data%</a>';
var HTMLworkDates = '<div class="date-text">%data%</div>';
var HTMLworkLocation = '<div class="location-text">%data%</div>';
var HTMLworkDescription = '<p><br>%data%</p>';

var HTMLprojectStart = '<div class="project-entry"></div>';
var HTMLprojectTitle = '<li class= project><h3>%data%</h3>';
var HTMLprojectDates = '<div class="date-text">%data%</div>';
var HTMLprojectDescription = '<p><br>%data%</p>';
var HTMLprojectURL = '<a href="#">%data%</a>';
var HTMLprojectImage = '<img src="%data%"></div></li>';

var HTMLschoolStart = '<div class="education-entry"></div>';
var HTMLschoolName = '<br><h4>%data%</h4>';
var HTMLschoolDegree = ' -- %data%</a>';
var HTMLschoolDates = '<div class="date-text">%data%</div>';
var HTMLschoolLocation = '<br><div class="location-text">%data%</div>';
var HTMLschoolMajor = '<p>%data%</p>';

var HTMLonlineClasses = '<br><h3>Online Classes</h3>';
var HTMLonlineTitle = '<br><h4>%data%</h4>';
var HTMLonlineSchool = ' - %data%:</a>';
var HTMLonlineDates = '<div class="date-text">%data%</div>';
var HTMLonlineURL = '<a href="#">%data%</a>';

var internationalizeButton = '<button>Internationalize</button>';
var googleMap = '<div id="map"></div>';



$(document).ready(function() {
  $('button').click(function() {
    var iName = inName() || function(){};
    $('#name').html(iName);  
  });
});



//Buider
var bio = {
	"name": "Anna Teglassy",
	"role": "painter - junior front-end developer",
	"contacts": {
		"email": "teglanna@gmail.com",
    	"github": "teglanna",
    	"twitter": "@teglanna",
    	"website" : "annateglassy.tumblr.com",
    	"location": "Budapest"
    },
    "welcomeMessage": "Hello-bello Everybody!",
    "skills": ["persistence","courage", "irony"],
    "pic": "images/anna.png"
}

var formattedName = HTMLheaderName.replace("%data%", bio.name);
$("#header").append(formattedName);

var formattedRole = HTMLheaderRole.replace("%data%", bio.role);
$("#header").append(formattedRole);

var formattedImage = HTMLbioPic.replace("%data%", bio.pic);
$("#header").append(formattedImage);

var formattedEmail = HTMLemail.replace("%data%", bio.contacts.email);
$("#header").append(formattedEmail);

var formattedTwitter = HTMLtwitter.replace("%data%", bio.contacts.twitter);
$("#header").append(formattedTwitter);

var formattedGitHub = HTMLgithub.replace("%data%", bio.contacts.github);
$("#header").append(formattedGitHub);

var formattedWebsite = HTMLblog.replace("%data%", bio.contacts.website);
$("#header").append(formattedWebsite);

var formattedLocation = HTMLlocation.replace("%data%", bio.contacts.location);
$("#header").append(formattedLocation);