/**
 * Created by zdvitas on 03.12.13.
 */
    $(document).ready(function(){
        $('#click_me').click(function(e){
            e.preventDefault()
            clear_quest_form()
            $.post('/ajax/add_task/', {'tittle': $('#id_tittle').val(), 'body' : $('#id_body').val() , 'csrfmiddlewaretoken' :$('#csrfmiddlewaretoken').val() }, function(){
                        $('#myModal').modal('hide')
                        location.reload()
                });

        });
    })

    function clear_quest_form() {

    }

    $('#myModal').on('show', function () {
         clear_quest_form()
})

    $('#modalAuth').on('show', function () {
         reset_login_form()
})

    function reset_login_form() {
        document.getElementById('id_email_div').style.display='none'
        document.getElementById('password_err').style.display='none'
        document.getElementById('user_err').style.display='none'
        document.getElementById('id_register').style.display = 'inline'
        document.getElementById('id_login').style.display = 'inline'
        document.getElementById('btn_register').style.display='none'
        document.getElementById("auth_err").style.display='none'
    }

    function set_login(username) {
        document.getElementById('id_username_head').innerText = username
        document.getElementById('id_username_head').style.display ='block'
        document.getElementById('btn_logout').style.display ='block'
        document.getElementById('btn_login').style.display ='none'
        document.getElementById('#ask').style.display ='block'

    }



    $('#id_register').click(function(e){
            e.preventDefault()
            document.getElementById("auth_err").style.display='none'
            document.getElementById('id_email_div').style.display='inline'
            document.getElementById('id_login').style.display = 'none'
            document.getElementById('id_register').style.display = 'none'
            document.getElementById('btn_register').style.display='inline'


        });

        $(document).ready(function(){
        $('#id_login').click(function(e){
            e.preventDefault()

            $.post('/ajax/login/', {'login': $('#id_username').val(), 'password' : $('#id_password').val()}, function(data){
                    data = $.parseJSON(data);

                    if(data['status'] == 'ok') {
                        $('#modalAuth').modal('hide')
                        document.getElementById('id_message_text').innerText = "Авторизация успешна!"
                        ///set_login(data['username'])
                        $('#modalMessage').modal('show')
                        setTimeout('location.reload()', 1000)

                        location.reload()
                    }
                    if(data['status'] == 'bad') {

                        if( data['login_err'] == 'not') {
                            document.getElementById('user_err').style.display = 'inline'
                        }
                        if( data['pass_err'] == 'not') {
                            document.getElementById('password_err').style.display = 'inline'
                        }
                    }
                    if(data['status'] == 'fail') {

                       document.getElementById('auth_err').style.display = 'inline'

                    }


                });

        });
    })


   $('.quest_up').click(function(e){
            e.preventDefault()
       alert($(this).attr("id"))

        });


    $('#id_register').click(function(e){
            e.preventDefault()
            document.getElementById('id_email_div').style.display='inline'
            document.getElementById('id_login').style.display = 'none'
            document.getElementById('id_register').style.display = 'none'
            document.getElementById('btn_register').style.display='inline'


        });

        $(document).ready(function(){
        $('#btn_register').click(function(e){
            e.preventDefault()

            $.post('/ajax/register/', {'login': $('#id_username').val(), 'password' : $('#id_password').val() ,
            'email' :$('#id_email').val()}, function(data){
                    data = $.parseJSON(data);

                    if(data['status'] == 'ok') {
                        $('#modalAuth').modal('hide')
                        document.getElementById('id_message_text').innerText = "Регистрация успешно завершена"
                        set_login(data['username'])
                        $('#modalMessage').modal('show')
                    } else {

                        if( data['login_err'] == 'not') {
                            document.getElementById('user_err').style.display = 'inline'
                        }
                        if( data['pass_err'] == 'not') {
                            document.getElementById('password_err').style.display = 'inline'
                        }
                        if( data['email_err'] == 'not') {
                            document.getElementById('email_err').style.display = 'inline'
                        }


                    }


                });

        });
    })

        $(document).ready(function(){
        $('#btn_logout').click(function(e){
            e.preventDefault()

            $.post('/ajax/logout/', {'login': $('#id_username').val(), 'password' : $('#id_password').val() ,
            'email' :$('#id_email').val()},function() {
                location.reload()
            });


        });
    })