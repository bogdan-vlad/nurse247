  function display_box_conviction() {
    let checkBox = document.getElementById("convicted_yes");
    let criminal = document.getElementById("criminal");
      if (checkBox.id == 'convicted_yes') {
        criminal.style.display = "block";
      }
  }

  function hide_box_conviction() {
    let criminal = document.getElementById("criminal");

    criminal.style.display = "none"
  }


  function display_investigation() {
    let suspension = document.getElementById("suspension_yes");
    let investigation = document.getElementById("investigation");

    if (suspension.id == 'suspension_yes') {
      investigation.style.display = 'block'
    }
  }

  function hide_display_conviction() {
    let investigation = document.getElementById("investigation");

    investigation.style.display = 'none';
  }

  function display_health_yes() {
    let health_yes = document.getElementById("health_yes");
    let health = document.getElementById("health");
    if (health_yes.id == 'health_yes') {
        health.style.display = 'block'
    }
  }

  function hide_health_yes() {
    let health = document.getElementById("health");

    health.style.display = 'none';
  }

  function preload() {
    let preloader = document.getElementById("preloader");

    preloader.style.display = 'block';
  }
