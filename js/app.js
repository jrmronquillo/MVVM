// Class to represent a row in the seat reservations grid
function DataClass(name, name2) {
    var self = this;
    self.name = name;
    self.title = ko.observable(name2);

    
}

// Overall viewmodel for this screen, along with initial state
function dataViewModel() {
    var self = this;

    // Non-editable catalog data - would come from the server
    self.jsonDataFromServer = [
        { title: "test_title_1" },
    ];    

    console.log(self.jsonDataFromServer[0]);
    // Editable data
    self.chosenData = ko.observableArray([
        new DataClass("Steve", self.jsonDataFromServer[0]),
    ]);
}

ko.applyBindings(new dataViewModel());