'use strict';

// app.module.js
var issueWiseMainModule = angular.module('issuewiseApp', [ 'ngResource', 'ngRoute', 'ngCookies', 'vcRecaptcha', 'pascalprecht.translate', 'tmh.dynamicLocale'])
  /*
   * ROUTES
   */
  .config(['$routeProvider','$translateProvider', function($routeProvider, $translateProvider) {
      $routeProvider.when('/', {templateUrl: 'views/index.html', controller: 'InitCtrl'});      
      $routeProvider.when('/login', {templateUrl: 'views/login.html', controller: 'LogInCtrl'});
      $routeProvider.when('/signup', {templateUrl: 'views/signup.html', controller: 'SignUpCtrl'});
      $routeProvider.when('/profile', {templateUrl: 'views/profile.html', controller: 'ProfileCtrl'});
      $routeProvider.otherwise({redirectTo: '/'});
      
      $translateProvider.useMissingTranslationHandlerLog();
      
      // required, please use your own key :)
      /*reCAPTCHAProvider.setPublicKey('6LfyK-0SAAAAAAl6V9jBGQgPxemtrpIZ-SPDPd-n');
      // optional
      reCAPTCHAProvider.setOptions({
    	  theme: 'clean'
      }); */
      
  }])
  .config(['$translateProvider', function ($translateProvider) {
    $translateProvider.useStaticFilesLoader({
        prefix: 'resources/locale-',// path to translations files
        suffix: '.json'// suffix, currently- extension of the translations
    });
    $translateProvider.preferredLanguage('en_US');// is applied on first load
    $translateProvider.useLocalStorage();// saves selected language to localStorage
  }])
  .constant('LOCALES', {
    'locales': {
        'ru_RU': 'Русский',
        'en_US': 'English'
    },
    'preferredLocale': 'en_US'
  })
  .config(function (tmhDynamicLocaleProvider) {
    tmhDynamicLocaleProvider.localeLocationPattern('lib/angular-1.3.14/i18n/angular-locale_{{locale}}.js');
  })
  .run(['$rootScope', '$location', '$cookieStore', '$http',
    function ($rootScope, $location, $cookieStore, $http) {
        // keep user logged in after page refresh
        $rootScope.globals = $cookieStore.get('globals') || {};
        if ($rootScope.globals.currentUser) {
            $http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentUser.authdata; 
        }
  
        $rootScope.$on('$locationChangeStart', function (event, next, current) {
            // redirect to login page if not logged in
            /*if (($location.path() == '/login' || $location.path() == '/signup' )) {
                
            } else if (!$rootScope.globals.currentUser){
            	
            } else {
            	$location.path('/');
            }*/
        });
    }]);


