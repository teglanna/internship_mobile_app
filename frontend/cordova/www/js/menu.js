var module = ons.bootstrap();
module.controller('AppController', ["$scope", function($scope) {
  ons.createPopover('popover.html').then(function(popover) {
    $scope.popover = popover;
  });

  $scope.show = function(e) {
    $scope.popover.show(e);
  };
}]);
