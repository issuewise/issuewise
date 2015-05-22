'use strict';

// Not sure if we really need wbVariable directive.

issueWiseMainModule.directive('ngTranslateLanguageSelect', function(LocaleService) {
	return {
		templateUrl : 'templates/selectedLanguageTpl.html',
		restrict : 'A',
		replace : true,
		scope : {
			variable : '=',
			type : '='
		},

		controller : function($scope) {
			 $scope.currentLocaleDisplayName = LocaleService.getLocaleDisplayName();
             $scope.localesDisplayNames = LocaleService.getLocalesDisplayNames();
             $scope.visible = $scope.localesDisplayNames &&
             $scope.localesDisplayNames.length > 1;
 
             $scope.changeLanguage = function (locale) {
                 LocaleService.setLocaleByDisplayName(locale);
             };
		}
	};
});
