function clearText() {
  let textForm = document.getElementsByClassName("text_field");
  Object.keys(textForm).forEach(function (element) {
    console.log(element);
    textForm[element].value = "";
  });
}
