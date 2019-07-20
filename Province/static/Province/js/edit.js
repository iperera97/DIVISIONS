// when edit page load view previous feature image
var featureImageBox = $("#feature-image");
var featureImageURL = featureImageBox.find("span").text()
var showImageBox = $("#show_image")


console.log(featureImageURL)

// has url)
if (featureImageURL) {

    // create image
    var image = $("<img>")
    image.attr("src", `/media/${featureImageURL}`)
    image.css({ "width": "200px" })

    console.log(image.attr("src"))
    showImageBox.append(image)
}

