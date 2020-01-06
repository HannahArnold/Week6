let quiz = JSON.parse(
  Get("https://opentdb.com/api.php?amount=10&category=27&type=multiple")
);
for (i = 0; i < 10; i++) {
  console.log(i + " " + quiz.results[i].question + "\n");
  let question = quiz.results[i].question;

  let body = document.getElementsByTagName('body')[0];
  body.innerHTML += quiz.results[i].question + "<br/>"
  console.log(quiz.results[0].question);
}
