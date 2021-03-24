//funcion asincrona para hacer un post en la base de datos
//comentario nuevo
async function register(nombre, apellido, user, password) {

    let result = await fetch("http://localhost:8080/post/newuser", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "id": user,
            "contra": password,
            "nombre" : nombre,
            "apellido" : apellido
        })
    })
    result = await result.json();
    console.log(result);
    alert(result.result);
    //if (!result.success) alert("FAILED! ")
}

function inputUser() {
    // variables para comprobar que todos los datos estan correctos
    let passcheck= false;
    let usercheck= false;
    // caraibles para almacenar los datos ingresados por el usuario

    const nombre = document.getElementById("name_id").value;
    const apellido = document.getElementById("secname_id").value;
    const password = document.getElementById("passw_id").value;
    const user = document.getElementById("usern").value;
    

    //si el ususario ingreso un nombre correcto y no existe en la base de datos se devuele un true
    if(user){
        usercheck= true;
    }
    // si no ingreso un nombre de usuario, alertar que ingrese uno
    else if(!user){
        usercheck= false;
        alert("Ingrese un nombre de Ususario");
    }
    //si no ingreso una contraseña se alerta al ususario
    if (!password) {
        alert("Ingrese una contraseña");
        passcheck= false
    }
    
    //si usercheck y passcheck son true, se hace el registro en la base de datos y se borran los datos 
    if(usercheck && passcheck){
        register(user, password, nombre, apellido)
        document.getElementById("name_id").value="";
        document.getElementById("secname_id").value="";
        document.getElementById("passw_id").value="";
        document.getElementById("usern").value="";
    }
}

const btn = document.getElementById("btn");
btn.addEventListener("click", inputUser);