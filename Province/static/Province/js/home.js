$("#province_table .delete").on("click", function (event) {
    var delteAncher = $(this)

    // get delete or not response
    var response = confirm("Are you shur to delete this province ?")

    if (!response) event.preventDefault()

})