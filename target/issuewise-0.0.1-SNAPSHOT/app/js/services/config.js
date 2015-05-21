'use strict';

issueWiseMainModule.config(function($provide) {
	$provide.constant("APP_CONTEXT_PATH", "");
	$provide.constant("REST_BASE_PATH", "");
})

/**
 * Common application configuration
 */
.factory('config', function(REST_BASE_PATH, APP_CONTEXT_PATH) {
	return {
		restBasePath : function() {
			return REST_BASE_PATH;
		},

		appContextPath : function() {
			return APP_CONTEXT_PATH;
		}
	};
});
