var tracks = document.querySelector("#tracks");
var copy = document.querySelector("#copy");

copy.addEventListener("click", function() {
  clipboard();
});

function clipboard() {
  tracks.select();
  document.execCommand("copy");
}
