var nombre_formulario_modal = ".frmEliminar"; //Clase

   // $(document).on('ready',function(){
        $(nombre_formulario_modal).submit(function(e){
            e.preventDefault();
        });

        var options = {
                success:function(response)
                {
                    if(response.statuse=="True"){
                        var idProd = response.product_id;
                            $('#tr'+idProd).remove();
                            $('#trr'+idProd).remove();

                        var subto = response.st;
                        var iva16 = response.iv;
                        var total = response.suma

                        $("#subt").text("Subtotal = "+subto)
                        $("#iva1").text("Iva = "+iva16)
                        $("#tota").text("Total = "+total)


                        $("#sumaba").text("Total = "+total)


                        var but = response.lo;
                        $("#cant").text(but)
                    }else{
                        alert("Hubo un error al eliminar!");
                    };
                }
            };

        $(nombre_formulario_modal).ajaxForm(options);
   // });