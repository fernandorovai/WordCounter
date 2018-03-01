// Script responsible for handling data between server and client.
// when button in pressed, send form using asynchronous method (ajax)
$(document).ready(function () {
    $("#mainForm").submit(function (event) {
        event.preventDefault(); // prevent default submission

        var formURL     = $(this).attr("action");
        var formMethod  = $(this).attr("method");
        var formData    = $(this).serializeArray();

        // add inserted text into inserted div just to keep tracking the text
        $("#insertedText").text("Inserted Text: " + $('#mainTextArea').val());

        // ajax request
        $.ajax({
            url: formURL,
            type: formMethod,
            data: formData,
            dataType: "json"
        }).done(function (response) {
            var errorMsg     = response['errorMsg'];
            var wordCounter  = response['wordCounter'];

            // Populate fields with server responses
            if(wordCounter == 0) $("#mainTextArea").val("");
            else $("#mainTextArea").val("You have inserted " + wordCounter + " word(s)");

            $("#errorMsg").text(errorMsg);

            // show / hide msg error div
            if(errorMsg != "") $('#errorMsg').fadeIn();
            else $('#errorMsg').fadeOut();

        })
    })
});