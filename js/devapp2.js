
/*jshint esversion: 6 */



// Class to represent a row in the seat reservations grid
function DataClass(name, name2) {
    var self = this;
    self.name = name;
    self.title = ko.observable(name2);

    
}

// Note: that the getJSON wraps the entire javascript body
//$.getJSON("js/dataList.json", function( jsonData ){
$.getJSON("http://10.23.223.39:5000/reporting/JSON?callback=?", function( jsonData ){
        const DataClass2 = function(data){
            this.name = ko.observable(data.title);
        };

// Overall viewmodel for this screen, along with initial state
function dataViewModel() {
    var self = this;

    console.log(jsonData.dataList);

    this.appError = ko.observable();  

    // Non-editable catalog data - would come from the server
    self.jsonDataFromServer = [
        { title: "test_title_1" },
    ];    

    // console.log(self.jsonDataFromServer[0]);
    // Editable data
    self.chosenData = ko.observableArray([
        new DataClass("Steve", self.jsonDataFromServer[0]),
        new DataClass("John", jsonData.dataList[0])
    ]);
    
    }
ko.applyBindings(new dataViewModel());

});