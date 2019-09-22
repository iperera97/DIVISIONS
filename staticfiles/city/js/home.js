const DISTRICT_TABLE = $("#city_table")

// when delete district record ask are u shur
DISTRICT_TABLE.find("#actions .delete a").on('click', function (event) {

    // create delete msg
    let deleteBtn = $(this);
    let deleteRecord = deleteBtn.parent().parent().parent();
    let deleteMSG = `Are you shur to delete (#${deleteRecord.find('.city_pk').text()}) ${deleteRecord.find('.city_eng').text()} City ?`;

    // if click delete true reuqest that endpoint
    var response = confirm(deleteMSG)
    if (!response) event.preventDefault()

})