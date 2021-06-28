function display() {
  var x = document.getElementById("uploadContainer");
  x.style.display = "block";
  x.style.margin = "0 0 0 5%";
}

function readURL(e) {
    if (e.files && e.files[0]) {
        var a = new FileReader;
        a.onload = function(e) { $("#imageResult").attr("src", e.target.result) }, a.readAsDataURL(e.files[0])
    }
}
// $(document).ready((function() { $("[data-bs-chart]").each((function(e, a) { this.chart = new Chart($(a), $(a).data("bs-chart")) })) })), $((function() { $("#upload").on("change", (function() { readURL(input) })) }));
var input = document.getElementById("upload"),
    infoArea = document.getElementById("upload-label");

function showFileName(e) {
    var a = e.srcElement.files[0].name;
    infoArea.textContent = "File name: " + a
}
input.addEventListener("change", showFileName),
    function(e) {
        "use strict";
        e('a.js-scroll-trigger[href*="#"]:not([href="#"])').click((function() { if (location.pathname.replace(/^\//, "") == this.pathname.replace(/^\//, "") && location.hostname == this.hostname) { var a = e(this.hash); if ((a = a.length ? a : e("[name=" + this.hash.slice(1) + "]")).length) return e("html, body").animate({ scrollTop: a.offset().top - 48 }, 1e3, "easeInOutExpo"), !1 } })), e(".js-scroll-trigger").click((function() { e(".navbar-collapse").collapse("hide") })), e("body").scrollspy({ target: "#mainNav", offset: 54 });
        var a = function() { e("#mainNav").offset().top > 100 ? e("#mainNav").addClass("navbar-shrink") : e("#mainNav").removeClass("navbar-shrink") };
        a(), e(window).scroll(a)
    }(jQuery);