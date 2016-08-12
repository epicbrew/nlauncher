(function() {
    'use strict';
    
    angular
        .module('nlauncher')
        .controller('ApplicationIndexController', ApplicationIndexController);

    ApplicationIndexController.$inject = ['appDataService'];
    
    function ApplicationIndexController(appDataService) {
        var vm = this;

        appDataService.getApplications().then(function(data) {
            vm.appGroups = data.groups;
            return vm.appGroups;
        });
    }
        
})();
