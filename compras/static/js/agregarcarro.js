// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla2 = "#tabla_productos"; // id
var nombre_boton_agregue = ".agregue"; // Clase
var nombre_formulario_modal2 = "#frmAgregar"; //id
var nombre_ventana_modal2 = "#myModal2"; // id
// Fin de configuraciones

    $(document).on('ready',function(){
        $(nombre_boton_agregue).on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idProducto2').val(Pid);
            $('#modal_name2').text(name);
        });

        var options = {
                success:function(response)
                {
                    if(response.statusa=="True"){

                        var cantidad = $("#cant").text();
                        cantid = parseInt(cantidad) + 1;
                        $('#cant').text(cantid);

                        //alert("agregado!");
                        var idProd = response.product_id2;
                        //$('#tr'+idProd).remove();
                        $('#tr'+idProd).append();
                        var namep = response.nombrep;
                        var repe = response.rep;

        var $ulLista;
        //si la lista html no existe entonces la agregamos al dom
        if(!$('#mario').find('ul').length) $('#mario').append('<ul/>');
        //obtenemos una instancia de la lista
        $ulLista=$('#divLista').find('ul');
        var $liNuevoNombre=$('<li/>').html("&nbsp;"+"&nbsp;"+repe+"&nbsp;"+"|"+"&nbsp;"+namep);
        $("#luigi").prepend($liNuevoNombre);





                        $(nombre_ventana_modal2).modal('hide');
                    }else{
                        //alert("Hubo un error al agregar!");
                        $(nombre_ventana_modal2).modal('hide');
                    };
                }
            };

        $(nombre_formulario_modal2).ajaxForm(options);
    });
