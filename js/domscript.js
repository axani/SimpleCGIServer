$(function() {

//     function confirmWindowclose() {
//         var inFormOrLink;
//         // $('a').on('click', function() { inFormOrLink = true; });
//         // $('form').bind('submit', function() { inFormOrLink = true; });

//         $(window).bind("beforeunload", function() { 
//             // return inFormOrLink || confirm("Do you really want to close?"); 
//             jQuery.ajax({
//                type: "POST",
//                url: "../cgi-bin/test.cgi",
//                success: function (msg) {
//                    alert("Data Saved: ");
//                }
// });
//         })
//     }

//     confirmWindowclose()
    
    $('#testlink').on('click', function() {
        $.ajax({
               type: "POST",
               url: "../cgi-bin/test.cgi",
               success: function (msg) {
                   alert("Yey! There Should be a txt-file in your folder!");
               }
        })  
    });

    console.log('hello');
});