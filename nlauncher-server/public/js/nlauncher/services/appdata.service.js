(function () {
    'use strict';

    angular.module('nlauncher')
        .factory('appDataService', appDataService);

    appDataService.$inject = ['$http'];

    function appDataService($http) {
        var service = {
            getApplications: getApplications
        };

        return service;

        function getApplications() {
            return $http.get('/applications')
                .then(getApplicationsComplete)
                .catch(getApplicationsFailed);

            function getApplicationsComplete(response) {
                //return response.data.results;
                console.log("got applications:", response.data);
                return response.data;
            }

            function getApplicationsFailed(error) {
                console.log('XHR Failed for getApplications.' + error.data);
            }
        }
    }

})();
