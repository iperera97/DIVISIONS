!function ($) {
	$(document).on("click", "ul.nav li.parent > a ", function () {
		$(this).find('em').toggleClass("fa-minus");
	});
	$(".sidebar span.icon").find('em:first').addClass("fa-plus");
}

	(window.jQuery);
$(window).on('resize', function () {
	if ($(window).width() > 768) $('#sidebar-collapse').collapse('show')
})

$(window).on('resize', function () {
	if ($(window).width() <= 767) $('#sidebar-collapse').collapse('hide')
})




// init variables
const NAVIGATION_LIST = $("#sidebar-collapse .nav li");
const CURRENT_ENDPOINT = location.pathname

// remove active class in all list elements
NAVIGATION_LIST.removeClass("active")

Array.from(NAVIGATION_LIST).forEach(function (ele) {

	// create key n value
	let listEle = $(ele)
	let endpointVALUE = listEle.find('a').attr('href')

	// add active class
	if (CURRENT_ENDPOINT == endpointVALUE) listEle.addClass('active')

})





