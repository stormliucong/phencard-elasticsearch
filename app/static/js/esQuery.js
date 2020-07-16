//Ready function when page is loaded
$(document).ready(function () {
    //Autocomplete function
    var autoCompleteDemo = function (query, cb) {
        var results = $.map([0], function () {
            //Get text from the input field
            var text = document.getElementById('typeahead').value;
            //ES Query
            var json = {
                "suggest": {
                    "name": {
                        "text": "cleft plate",
                        "completion": {
                            "field": "NAMESUGGEST",
                            "fuzzy": {
                                "fuzziness": 1
                            },
                            "skip_duplicates": true,
                            "size": 10
                        }
                    }
                }
            };

            //Ajax call to ES make sure this matches YOUR ES info
            var request = $.ajax({
                type: "POST",
                url: "http://localhost:9200/autosuggest/_search",
                async: false,
                data: JSON.stringify(json),
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (data) {
                    return (data);
                },
                failure: function (errMsg) {
                    alert(errMsg);
                }
            });

            //Parse the results and return them
            var response = JSON.parse(request.responseText);
            var resultsArray = response.suggest.name[0].options;
            var datum = [];
            for (var i = 0; i < resultsArray.length; i++) {
                datum.push({
                    theValue: resultsArray[i].text
                });
            }
            return datum;
        });

        cb(results);
    };

    alert('something!')

    $('.typeahead').typeahead(null, {
        displayKey: 'theValue',
        source: autoCompleteDemo
    });

    alert('something!');
    $(function () {
        $("#typeahead").autocomplete({
            source: function (request, response) {
                var arr = new Array();
                var postData = {
                    "suggest": {
                        "name": {
                            "text": "cleft plate",
                            "completion": {
                                "field": "NAMESUGGEST",
                                "fuzzy": {
                                    "fuzziness": 1
                                },
                                "skip_duplicates": true,
                                "size": 10
                            }
                        }
                    }
                };

                $.ajax({
                    type: "POST",
                    url: "http://localhost:9200/autosuggest/_search",
                    async: false,
                    data: JSON.stringify(postData),
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    success: function (data) {
                        var resultsArray = (data.suggest.name[0].options);
                        for (var i = 0; i < resultsArray.length; i++) {
                            arr.push(resultsArray[i].text);
                        }
                        response(arr);
                    },
                    failure: function (errMsg) {
                        alert(errMsg);
                    }
                });
            },
            minLength: 3, delay: 300
        })
    });


});


