//conecion a postgresql
const { Pool } = require('pg')

//dot env para el manejo de links
require('dotenv').config()

const connectionString = process.env.URL

const pool = new Pool({
  connectionString,
})

module.exports = pool;