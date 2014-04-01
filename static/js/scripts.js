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


    $(document).ready(function(){
        $('#btn_login').click(function(e){
            e.preventDefault()
            document.getElementById("auth_err").style.display='none';
            $.post('/login/', {'Email': $('#Email').val(), 'Password' : $('#Password').val()  }, function(data){
                         data = $.parseJSON(data)
                         if(data["status"]=="FAIL"){
                            document.getElementById("auth_err").style.display='inline';
                         } else
                         {
                             location.reload()


                         }
                });

        });
    })















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

