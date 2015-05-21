'use strict';

issueWiseMainModule.controller('SignUpCtrl', ['$scope', '$rootScope', '$location', 'AuthenticationSignUpService', 'vcRecaptchaService',
   function ($scope, $rootScope, $location, AuthenticationSignUpService, recaptcha) {
	
	$scope.user = {};

	AuthenticationSignUpService.ClearCredentials();
    
    $scope.signup = function () {
        $scope.dataLoading = true;
        AuthenticationSignUpService.Signup($scope.username, $scope.email, $scope.password1, $scope.password2, function(response) {
            if(response.success) {
            	//AuthenticationSignUpService.SetCredentials($scope.username, $scope.password);
            	
            	/*if($scope.registerForm.$valid) {
                    $scope.showdialog = true;
                    console.log('Form is valid');
                }*/
            	
                $location.path('/profile');
            } else {
                $scope.error = response.message;
                $scope.dataLoading = false;
            }
        });
    };
    
    $scope.register = function () {
        if($scope.registerForm.$valid) {
            $scope.showdialog = true;
            console.log('Form is valid');
        }
    };
    
    $scope.setWidgetId = function (widgetId) {
        // store the `widgetId` for future usage.
        // For example for getting the response with
        // `recaptcha.getResponse(widgetId)`.
    };

    $scope.setResponse = function (response) {
        // send the `response` to your server for verification.
    };
    
    
}]);
