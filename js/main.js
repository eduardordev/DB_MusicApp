const pg = require('pg')
const connectionString = "postgres://postgres:456528@localhost/127.0.0.1:58133/nameOfDatabase/proyecto1"

const client = new pg.Client(connectionString);

client.connect();

