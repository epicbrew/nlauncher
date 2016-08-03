(function() {
    'use strict';
    
    angular
        .module('nlauncher')
        .controller('ApplicationIndexController', ApplicationIndexController);

    ApplicationIndexController.$inject = ['appDataService'];
    
    function ApplicationIndexController(appDataService) {
        var vm = this;

        console.log("ApplicationIndexController: construct");

        appDataService.getApplications().then(function(data) {
            vm.appGroups = data.groups;
            return vm.appGroups;
        });
    }
        
})();
