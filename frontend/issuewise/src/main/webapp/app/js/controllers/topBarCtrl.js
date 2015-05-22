'use strict';

issueWiseMainModule.controller('TopBarCtrl', ['$scope', function($scope) {
	
	$scope.topbars = {
			url_logo_image : "http://www.issuewise.com/url_logo_image",
			url_home_icon : "http://www.issuewise.com/url_home_icon",
			url_home : "http://www.issuewise.com/url_home",
			url_user_picture : "http://www.issuewise.com/url_user_picture",
			notifications: [{
			      friend_notification_icon: "http://www.issuewise.com/url_user_picture",
			      friend_notification: "3",
			      follow_notification_icon: "http://www.issuewise.com/follow_notification_icon",
			      follow_notification: "4",
			      manifesto_notification_icon: "http://www.issuewise.com/manifesto_notification_icon",
			      manifesto_notification: "5",		      
			}]
		};
	
}]);
