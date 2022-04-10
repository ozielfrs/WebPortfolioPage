window.onload = (function () {
    var counter = 1;
    thisInterval = setInterval(function () {
        if (counter <= 16)
            $("div#success-page img#animate").attr("src", "/static/media/animation/success" + ("0000" + counter++).slice(-4) + ".png")
        else
            clearInterval(thisInterval)
    }, 50)
})