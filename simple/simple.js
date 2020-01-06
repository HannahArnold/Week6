let XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

function Get(url) {
  let Httppreq = new XMLHttpRequest();
  Httppreq.open("GET", url, false);
  Httppreq.send(null);
  return Httppreq.responseText;
}

let quiz = JSON.parse(
  Get("https://opentdb.com/api.php?amount=10&type=multiple")
);

for (i = 0; i < 10; i++) {
  console.log(i + " " + quiz.results[i].question + "\n");
}
