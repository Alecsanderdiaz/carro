// // Autor: @jqcaper
// // Configuraciones Generales
// var nombre_tabla2 = "#tabla_productos"; // id
// var nombre_boton_agregue3 = ".agregue3"; // Clase
// var nombre_formulario_modal2 = "#frmAgregar3"; //id
// var nombre_ventana_modal2 = "#myModal3"; // id
// // Fin de configuraciones

//     $(document).on('ready',function(){
//         $(nombre_boton_agregue3).on('click',function(e){
//             e.preventDefault();
//             var Pid = $(this).attr('id');
//             var name = $(this).data('name');
//             $('#modal_idProducto3').val(Pid);
//             $('#modal_name3').text(name);
//         });

//         var options = {
//                 success:function(response)
//                 {   alert(response.statusa3)
//                     if(response.statusa3=="True"){
//                         //alert("agregado!");
//                         var idProd = response.product_id3;

//                             $('#tr'+idProd).append();
//                             $(nombre_ventana_modal2).modal('hide');

//                     }else{
//                         //alert("Hubo un error al agregar!");
//                         $(nombre_ventana_modal2).modal('hide');
//                     };
//                 }
//             };

//         $(nombre_formulario_modal2).ajaxForm(options);
//     });