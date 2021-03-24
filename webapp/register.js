//funcion asincrona para hacer un post en la base de datos
//comentario nuevo
async function register(user, password) {

    let result = await fetch("http://localhost:8080/post/newuser", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "user": user,
            "password": password
        })
    })
    result = await result.json();
    console.log(result);
    alert(result.result);
    //if (!result.success) alert("FAILED! ")
}