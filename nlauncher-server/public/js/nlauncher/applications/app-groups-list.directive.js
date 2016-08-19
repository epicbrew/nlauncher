(function () {
    angular
        .module('nlauncher')
        .directive('appGroupsList', appGroupsList);

    function appGroupsList() {
        var directive = {
            templateUrl: 'js/nlauncher/applications/app-groups-list.directive.html',
            restrict: 'E',
            controller: AppGroupsListController,
            controllerAs: 'vm',
            bindToController: true
        };

        return directive;
    }

    AppGroupsListController.$inject = ['appDataService'];
    
    function AppGroupsListController(appDataService) {
        var vm = this;

        appDataService.getApplications().then(function(data) {
            vm.appGroups = data.groups;
            return vm.appGroups;
        });
    }

})()
