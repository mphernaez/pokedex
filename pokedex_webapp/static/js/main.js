$('#edit-pokemon').click(function(){
    $('#details').addClass('d-none')
    $('#details-edit').removeClass('d-none')
})

$('#cancel-edit').click(function(){
    $('#details').removeClass('d-none')
    $('#details-edit').addClass('d-none')
})

$('#submit-form').click(function(){
    if($('#sub-type-selection').val() == $('#main-type-selection').val()){
        $('#type-error').html('Main-type and Sub-type cannot be the same')
        return false
    } else {
        var data = {
            'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val(),
            'name': $('#pokemon-name').val(),
            'main_type': $('#main-type-selection').val(),
            'sub_type': $('#sub-type-selection').val()
        };
        console.log(data)
        $.ajax({
            url: "http://localhost:8000/pokemon/" + $('#pokemon-id').val() + "/",
            type: "post",
            data: data ,
            success: function (response) {
                Swal.fire({
                    icon: 'success',
                    title: 'Nice!',
                    text: 'You have successfully edited this Pokemon!',
                  })
                  setTimeout(function(){
                    window.location.reload();
                  }, 2000)
                  
            },
            error: function(jqXHR, textStatus, errorThrown) {
               console.log(textStatus, errorThrown);
               
            }
        });
    }
    swal("Successfully edited Pokemon", "success")
})