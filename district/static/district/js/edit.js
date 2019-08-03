const DISTRICT_FORM = $("#district-form")
const FEATURE_IMAGE_BLOCK = DISTRICT_FORM.find("#feature-image-block");
const IMAGE_URL = `/media/${FEATURE_IMAGE_BLOCK.data('feature-url')}`;

// create new image
let featureIMG = $("<img>");
featureIMG.attr('src', IMAGE_URL)
featureIMG.css({ 'width': '100%' })

FEATURE_IMAGE_BLOCK.append(featureIMG)
