// app.js
function run() {
  const kw = document.getElementById("kw").value;
  fetch(`/analyze?kw=${encodeURIComponent(kw)}`)
    .then(r => r.json())
    .then(d => {
      document.getElementById("out").textContent =
        JSON.stringify(d, null, 2);
    });
}
