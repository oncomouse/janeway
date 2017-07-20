function add_role(user_id, role_id, journal_id){
    data = {
        'user': user_id,
        'role': role_id,
        'journal': journal_id
    }
    var enrol_type = $('#enrol_type').val();
    $.ajax({
        "type": "POST",
        "dataType": "json",
        "url": '/api/accountrole/',
        "data": data,
        "success": function(data) {
            console.log(data)
            var user_row = $("#" + user_id ).clone();
            $("#" + user_id ).remove()
            user_row.find('td:first').html('<input name="' + enrol_type + '" value="' + user_id + ' " type="radio">')
            user_row.find('td:last').html('0')
            $('#reviewers tbody').append(user_row);
            toastr.success('User has been granted role.')
        },
        "error": function (xhr, status, error) {
            toastr.error(xhr.responseText)
        },
    })
}