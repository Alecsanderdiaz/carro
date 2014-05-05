
var nombre_formulario_modal2 = ".frmAgregar"; //clase

  //$(document).ready(function(){
    $(nombre_formulario_modal2).submit(function(e){
      e.preventDefault();
    });

    var options = {
      success:function(response){

        if(response.statusa=="True")
        {
          var cantidad = $("#cant").text();
          cantid = parseInt(cantidad) + 1;
          $('#cant').text(cantid);
          var namep = response.nombrep;
          var repe = response.rep;
          var preciott = response.preciot;
          var idProd = response.product_id2;
          var amen = '#tr'+idProd;
          var bas = '#trr'+idProd;
          var bate = 'trr'+idProd;

          if ($(bas).length)
          {
            $(bas).find("td:first").text(repe);
          } 
          else 
          {
            $("#tabase").find('tbody')
                .append($('<tr id="bas">')
                    .append($('<td>')
                            .text(repe)
                        )
                    .append($('<td>')
                            .text(namep)
                        )
                    .append($('<td>')
                            .text()
                        )
                    );
            $("#bas").attr("id",bate);
          }
          $(amen).find("td:first").text(repe);
          $(amen).find("td:last").text(preciott);

          var subto = response.st;
          var iva16 = response.iv;
          var total = response.suma;

          $("#subt").text("Subtotal = "+subto);
          $("#iva1").text("Iva = "+iva16);
          $("#tota").text("Total = "+total);

          $("#sumaba").text("Total = "+total);

          var but = response.lo;
          $("#cant").text(but);
        }
        else
        {
          alert("No tenemos la cantidad en inventario");
        }

        
      }
    };

    $(nombre_formulario_modal2).ajaxForm(options);
 // });
