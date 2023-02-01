function getResponse() {
    let userText = $("#textInput").val()
    let userHtml = '<div class="chat self"><div class="user-photo"><img src="../static/images/self.png"></div><p class="chat-message">' + userText + '</p></div>';
    $("#textInput").val("");
    $("#chatlogs").append(userHtml);
    $('#chatlogs').animate({
        scrollTop: $('#chatlogs')[0].scrollHeight}, "slow");

$.get("/get", { msg: userText }).done(function(data) {
      var botHtml = '<div class="chat bot"><div class="user-photo"><img src="../static/images/bot.png"></div><p class="chat-message">' + data + '</p></div>';
      $("#chatlogs").append(botHtml);
    });
    $('#chatlogs').animate({
        scrollTop: $('#chatlogs')[0].scrollHeight}, "slow");
};
$("#textInput").keypress(function(e) {
    //if enter key is pressed
    if(e.which == 13) {
        getResponse();
    }
});
$("#buttonInput").click(function() {
    getResponse();
});
