$( document ).ready(function() {

    $("#url_shortener_form").submit(function() {

        var url = "/shorten";

        $.ajax({
               type: "POST",
               url: url,
               data: $("#url_shortener_form").serialize(),
               success: function(data)
                {
                    console.log(data);

                    $('.parsed_url').text('Success! Your shortened URL is ' + data);
                }
             });

        return false;
    });

});