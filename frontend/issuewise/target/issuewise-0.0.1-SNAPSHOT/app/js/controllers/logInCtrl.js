'use strict';

issueWiseMainModule.controller('LogInCtrl', ['$scope', '$rootScope', '$location', 'AuthenticationLogInService',
    function ($scope, $rootScope, $location, AuthenticationLogInService) {
        	AuthenticationLogInService.ClearCredentials();
                                               
            $scope.login = function () {
                          $scope.dataLoading = true;
                          AuthenticationLogInService.Login($scope.username, $scope.password, function(response) {
                          if(response.success) {
                        	  AuthenticationLogInService.SetCredentials($scope.username, $scope.password);
                                $location.path('/profile');
                          } else {
                                $scope.error = response.message;
                                $scope.dataLoading = false;
                          }
                   });
            };
}]);
