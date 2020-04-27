  function display_box_conviction() {
    let checkBox = document.getElementById("convicted_yes");
    let criminal = document.getElementById("criminal");
      if (checkBox.id == 'convicted_yes') {
        criminal.style.display = "block";
      }
  }

  function display_investigation() {
    let suspension = document.getElementById("suspension");
    let investigation = document.getElementById("investigation");

    if (suspension.id == 'suspension') {
      investigation.style.display = 'block'
    }
  }

  function hide_box_conviction() {
    let criminal = document.getElementById("criminal");

    criminal.style.display = "none"
  }