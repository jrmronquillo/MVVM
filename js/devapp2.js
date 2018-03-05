
/*jshint esversion: 6 */



// Class to represent a row in the seat reservations grid
function DataClass(name2) {
    var self = this;
    //self.name = name;
    self.title = ko.observable(name2.data);
    //self.title = name2;
    
}

// Note: that the getJSON wraps the entire javascript body
//$.getJSON("js/dataList.json", function( jsonData ){
$.ajax({
    url: 'http://10.23.223.39:5000/reporting/JSON',
    dataType: 'JSONP',
    jsonpCallback: 'callback',
    type: 'GET',
    success: function (jsonPdata) {
        console.log(jsonPdata.dataList);
        // Overall viewmodel for this screen, along with initial state
        function dataViewModel() {
            var self = this;

            console.log(jsonPdata.dataList[0].data);

            this.testCaseData = ko.observableArray([]);

            // Non-editable catalog data - would come from the server
            self.jsonDataFromServer = [
                { data: "test_title_1" },
            ];    

            jsonPdata.dataList.forEach(function(item){
                self.testCaseData.push( new DataClass ( item ) );
            })
            // console.log(self.jsonDataFromServer[0]);
            // Editable data
            self.chosenData = ko.observableArray([
                new DataClass("Steve", self.jsonDataFromServer[0]),
                new DataClass("John", jsonPdata.dataList[0])
            ]);
    
            }
        ko.applyBindings(new dataViewModel());
    },
    error: function(failData){
        alert(failData);
        alert("Could not retrieve JSON data");
    }



});