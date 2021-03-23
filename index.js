const {Client} = require('pg')
const client = new Client ({
	user: "postgres",
	password: "12345",
	host: "localhost",
	port: 5432,
	database: "Proyecto"
})

client.connect()
.then(() => console.log("Conected seccessfully"))
.then(() => client.query("select * from musica"))
.then(results => console.table(results.rows))
.catch(e => console.error)
.finally(() => client.end())