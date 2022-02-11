console.log("polls.js");

//$ je jQuery root objekt

function getPollWrapperElementByPollId(pollId) {
  // check https://api.jquery.com/category/selectors/
  var pollSection = $('.poll-section[data-poll="' + pollId + '"]');
  return pollSection;
}

function onPollPostSuccess(votedPoll) {
  var pollSection = getPollWrapperElementByPollId(votedPoll.id);
  console.log(votedPoll);
  for (var i = 0; i < votedPoll.choices.length; i++) {
    var choice = votedPoll.choices[i];

    var voteButton = pollSection.find(
      '.vote-button[data-choice="' + choice.id + '"]'
    );
    voteButton.attr("disabled", true);
    voteButton.text(choice.choice_text + ": " + choice.votes);
    console.log(choice, voteButton);

    Cookies.set('Polls', 'true', { expires: 7, sameSite: 'none', Secure: true })
  }
}

// button bind: https://api.jquery.com/on/
$(".vote-button").on("click", function () {
  var button = $(this);
  var pollId = button.data("poll"); //data-poll
  var choiceId = button.data("choice"); //data-choice
  var url = "/api/polls/" + pollId + "/vote/";
  var paylaod = {
    choice: choiceId,
  };
  //   console.log("Sending", paylaod, "to", url);

  // send ajax POST call to API
  // on success, do onPollPostSuccess
  $.ajax({
    type: "POST",
    url: url,
    data: paylaod,
    success: onPollPostSuccess,
    dataType: "json"
  });
});

var pollsCookie = Cookies.get('Polls')

if(pollsCookie){
  var element = document.getElementsByClassName('vote-button');
  for (i = 0; i < element.length; i++){
    element[i].disabled = true
  }
}
