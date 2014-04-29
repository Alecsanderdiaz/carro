// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla2 = "#tabla_productos"; // id
var nombre_boton_agregue = ".agregue"; // Clase
var nombre_formulario_modal2 = ".frmAgregar"; //id
var nombre_ventana_modal2 = "#myModal2"; // id
// Fin de configuraciones

    //$(document).on('ready',function(){
        $(nombre_formulario_modal2).submit(function(e){
            e.preventDefault();
            // var Pid = $(this).attr('id');
            // var name = $(this).data('name');
            // $('#modal_idProducto2').val(Pid);
            // $('#modal_name2').text(name);
        });

        var options = {
                success:function(response)
                {
                    if(response.statusa=="True"){

                        var cantidad = $("#cant").text();
                        cantid = parseInt(cantidad) + 1;
                        $('#cant').text(cantid);

                        var namep = response.nombrep;
                        var repe = response.rep;
                        var preciott = response.preciot;

                        //alert("agregado!");
                        var idProd = response.product_id2;
                        //var row = '#tr'+idProd;
                        var amen = '#tr'+idProd;
                        var bas = '#trr'+idProd;
// Tratando de acomodar el boton
                        //$('#tabase > tbody:last').append('<tr id=bas ><td></td></tr>');
                        //$(bas).find("td:first").text(repe);
                        //$(bas).find("td:second").text(namep);

// FIN Tratando de acomodar el boton
                        //alert(amen);
                        $(amen).find("td:first").text(repe);
                        $(amen).find("td:last").text(preciott);

                        $(bas).find("td:first").text(repe);
                        //$(amen).find("td:last").text(preciott);


                        var subto = response.st;
                        var iva16 = response.iv;
                        var total = response.suma

                        $("#subt").text("Subtotal = "+subto)
                        $("#iva1").text("Iva = "+iva16)
                        $("#tota").text("Total = "+total)

                        $("#sumaba").text("Total = "+total)

                        var but = response.lo;
                        $("#cant").text(but)


    
//First, obtain the td that contains 'Value2'
// var $tdThatContainsMora = $("#tabla_productos tr td").filter(function(){
//     return $(this).html() == "Mora";
// });
// //Then, obtain the first td in its row (it's first 'sibling');
// $firstCellOfMorarow = $tdThatContainsMora.siblings("td").eq(0);
// alert($firstCellOfMorarow.html()); 

//$('#tabla_productos tr:nth-child(2) td:nth-child(1)').html('foo');
//$($('#tabla_productos').find('tbody>tr')[1]).children('td')[1].innerHTML = texto a cambiar;
                        //$(nombre_tabla2).append('<tr><td>"repe"</td><td></td><td>namep</td><td></td></tr>');
// var table = document.getElementById(tabla_productos);
// var row = table.insertRow(0);
// var cell1 = row.insertCell(0);
// var cell2 = row.insertCell(1);
// var cell3 = row.insertCell(2);
// var cell4 = row.insertCell(3);
// cell1.innerHTML = repe;
// cell2.innerHTML = "NEW CELL2";
// cell3.innerHTML = namep;
// cell4.innerHTML = "NEW CELL2";


// agregar en la lista boton

        // var $ulLista;
        // //si la lista html no existe entonces la agregamos al dom
        // if(!$('#mario').find('ul').length) $('#mario').append('<ul/>');
        // //obtenemos una instancia de la lista
        // $ulLista=$('#mario').find('ul');
        // var $liNuevoNombre=$('<li/>').html("&nbsp;"+"&nbsp;"+repe+"&nbsp;"+"|"+"&nbsp;"+namep);
        // $("#luigi").prepend($liNuevoNombre);





                        $(nombre_ventana_modal2).modal('hide');
                    }else{
                        //alert("Hubo un error al agregar!");
                        $(nombre_ventana_modal2).modal('hide');
                    };
                }
            };

        $(nombre_formulario_modal2).ajaxForm(options);
    //});
