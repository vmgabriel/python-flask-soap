function agregarNumero(val) {
    document.getElementById("resultado").value += val;
};

function operacionActivada(ope) {
    if (document.getElementById("resultado").value.trim() == "") {
        document.getElementById("valor").value = "0 " + ope;
    } else {
        document.getElementById("valor").value = document.getElementById("resultado").value.replace(" ","") + " " + ope;
    }
    document.getElementById("resultado").value = "";
    document.getElementById("resultado").focus();
};

function soloNumeros(e) {
    var key = window.Event ? e.which : e.keyCode;
	  return (key >= 48 && key <= 57) || (key == 8);
};

function borrar() {
    document.getElementById("resultado").value = "";
    document.getElementById("valor").value = "";
    document.getElementById("resultado").focus();
}
