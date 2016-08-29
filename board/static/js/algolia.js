// Needed for Algolia setup
var client = algoliasearch('SDMCCB8HOO', 'a5314e979ae881a0cf7154f9a9e78462');
var index = client.initIndex('post_test');

// Fetch search terms input on the index page
var searchTerm = localStorage.getItem("userInput");

var numResults = 0;
var nextTerm = "";
var processTime = 0;

$(document).ready(function() {
  $('input').keyup(function() {
    index.search($('input').val(), searchCallback);
  });
});


function searchCallback(err, content) {
    if (err) {
      console.error(err);
      return;
    }

    $('#resultList').empty();
    $("#resultSum").empty();

    if (content.query !== "") {
        for (var i = 0; i < content.hits.length; i++) {
           $(document).ready( $('#resultList').append(
            '<p style="font-size: 20px;">' + '<a href=' + '"' + content.hits[i].link + '"' + ' style=" color: rgba(76, 110, 158, 1);" >' + content.hits[i].title + '</a>' + '</p>'
            + '<p style=" color: rgba(99, 25, 45, .5);" >' + content.hits[i].link + '</p>' 
            + '<p style=" color: #a1a1a1;">' + content.hits[i].publisher + ' | ' + content.hits[i].date 
            + '</p>'
            + '<br/><br/>' 
            ));
        }
      numResults = content.nbHits;
      nextTerm = content.query;
      processTime = (content.processingTimeMS / 1000);
      $("#resultSum").empty().append(numResults, " results for '", nextTerm, "'" )
    } 
  };