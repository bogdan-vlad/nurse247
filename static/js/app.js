function display_box_conviction() {
    let checkBox = document.getElementById("convicted_yes");
    let text = document.getElementById("text");
      if (checkBox.id == 'convicted_yes') {
        text.style.display = "block";
      } else {
        text.style.display = "none";
      }
  }

  function hide_box_conviction() {
    let text = document.getElementById("text");

    text.style.display = "none"
  }