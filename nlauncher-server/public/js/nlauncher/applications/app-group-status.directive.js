(function () {
    angular
        .module('nlauncher')
        .directive('appGroupStatus', appGroupStatus);

    function appGroupStatus() {
        var directive = {
            templateUrl: 'js/nlauncher/applications/app-group-status.directive.html',
            restrict: 'E',
            link: linkFunc,
            controller: AppGroupStatusController,
            controllerAs: 'vm',
            bindToController: true,
            scope: {
                group: '='
            }
        };

        return directive;

        function linkFunc(scope, el, attr, ctrl) {
            console.log('LINK: group: %s', scope.vm.group)
            console.log('LINK: group.name: %s', scope.vm.group.name)
            console.log('LINK: group.application: %s', scope.vm.group.applications[0].name)
        }
    }

    function AppGroupStatusController() {
        var vm = this;
    }

})()
