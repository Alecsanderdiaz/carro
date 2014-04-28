// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla = "#tabla_productos"; // id
var nombre_boton_eliminar = ".delete"; // Clase
var nombre_formulario_modal = ".frmEliminar"; //id
var nombre_ventana_modal = "#myModal"; // id
// Fin de configuraciones

   // $(document).on('ready',function(){
        $(nombre_formulario_modal).submit(function(e){
            e.preventDefault();
            // var Pid = $(this).attr('id');
            // var name = $(this).data('name');
            // $('#modal_idProducto').val(Pid);
            // $('#modal_name').text(name);
        });

        var options = {
                success:function(response)
                {
                    if(response.statuse=="True"){
                        //alert("Eliminado!");
                        var idProd = response.product_id;
                            $('#tr'+idProd).remove();
                            //alert('#tr'+idProd)
                            $(nombre_ventana_modal).modal('hide');


                            //
                        var subto = response.st;
                        var iva16 = response.iv;
                        var total = response.suma

                        $("#subt").text("Subtotal = "+subto)
                        $("#iva1").text("Iva = "+iva16)
                        $("#tota").text("Total = "+total)
                        //
                    }else{
                        //alert("Hubo un error al eliminar!");
                        $(nombre_ventana_modal).modal('hide');
                    };
                }
            };

        $(nombre_formulario_modal).ajaxForm(options);
   // });