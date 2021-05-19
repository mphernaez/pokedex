$('#edit-pokemon').click(function(){
    $('#details').addClass('d-none')
    $('#details-edit').removeClass('d-none')
})

$('#delete-pokemon').click(function(){
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
      }).then((result) => {
        if (result.isConfirmed) {
          $.ajax({
            url: "http://localhost:8000/pokemon/" + $('#pokemon-id').val(),
            type: "delete",
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
            },
            success: function (response) {
                Swal.fire({
                    icon: 'success',
                    title: 'Deleted Pokemon!',
                    text: 'You have successfully deleted this Pokemon!',
                  })
                  setTimeout(function(){
                    location.href = "http://localhost:8000/pokemon/"
                  }, 2000)
                  
            },
            error: function(jqXHR, textStatus, errorThrown) {
               console.log(textStatus, errorThrown);
               
            }
        });
        }
      })
})

$('#cancel-edit').click(function(){
    $('#details').removeClass('d-none')
    $('#details-edit').addClass('d-none')
})

var url = $(this).data('base-url')

$('#submit-edit-form').click(function(){
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
        console.log( $(this).data('base-url'))
        $.ajax({
            url: url,
            type: "post",
            data: data ,
            success: function (response) {
                if ($('#pokemon-sprite-upload').val() != ''){
                    formdata = new FormData()
                    formdata.append('sprite', $('#pokemon-sprite-upload').prop('files')[0])
                    console.log(formdata)
                    console.log(url + '/upload-sprite/')
                    $.ajax({
                        url: 'upload-sprite/',
                        type: "post",
                        data: formdata,
                        processData: false,
                        contentType: false,
                        beforeSend: function(xhr) {
                            xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
                        },
                        success: function (response) {
                           
                        }
                    })
                }
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
})

$('#submit-create-form').click(function(){
    if($('#sub-type-selection').val() == $('#main-type-selection').val()){
        $('#type-error').html('Main-type and Sub-type cannot be the same')
        return false
    } else if ($('#pokemon-name').val() == ''){
        $('#type-error').html('Please input a name for Pokemon')
        return false
    } else if ($('#pokemon-sprite-upload').val() == ''){
        $('#type-error').html('Please select a sprite for your Pokemon')
        return false
    }else {
        var data = {
            // 'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val(),
            'name': $('#pokemon-name').val(),
            'main_type': $('#main-type-selection').val(),
            'sub_type': $('#sub-type-selection').val()
        };
        console.log(data)
        console.log( $(this).data('base-url'))
        $.ajax({
            url: "/pokemon/create/",
            type: "post",
            data: data ,
            // contentType: 'application/json',
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
            },
            success: function (data) {
                // console.log(data.id)
                data = JSON.parse(data)
                if ($('#pokemon-sprite-upload').val() != ''){
                    formdata = new FormData()
                    formdata.append('sprite', $('#pokemon-sprite-upload').prop('files')[0])
                    console.log(formdata)
                    console.log(url + '/upload-sprite/')
                    $.ajax({
                        url: "/pokemon/" + data['id'] + "/upload-sprite/",
                        type: "post",
                        data: formdata,
                        processData: false,
                        contentType: false,
                        beforeSend: function(xhr) {
                            xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
                        },
                        success: function (response) {
                           
                        }
                    })
                }
                Swal.fire({
                    icon: 'success',
                    title: 'Nice!',
                    text: 'You have successfully created a Pokemon!',
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
})

$('#pokemon-sprite-upload').change(function(){
    console.log($(this).val())

    if (this.files && this.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#pokemon-sprite-edit').attr('src', e.target.result);
        }
        reader.readAsDataURL(this.files[0]);
    }
})

$('#reset-sprite').click(function(){
    $('#pokemon-sprite-edit').attr('src', $('#pokemon-sprite-edit').data('current-sprite'));
    $('#pokemon-sprite-upload').val('')
})

$('#add-button').click(function(){
    $('#create-pokemon').removeClass('d-none')
    $('#pokemon-list').addClass('d-none')

})
