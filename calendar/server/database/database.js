//require('dotenv').config()
import * as dotenv from 'dotenv' 
//const { Client } = require("pg");
import pg from 'pg'

const { Client } = pg
dotenv.config()

const credentials ={
  host: 'localhost',
  user: process.env.POSTGRES_USER,
  port: 5432,
  password: process.env.POSTGRES_PW,
  database: process.env.POSTGRES_DB
}

async function clientDemo() {
    const client = new Client(credentials);
    await client.connect();
    const now = await client.query("SELECT NOW()");
    await client.end();
  
    return now;
  }

  (async () => {
    const clientResult = await clientDemo();
    console.log("Time with client: " + clientResult.rows[0]["now"]);
  })();
  
// client.connect();
// client.query(`select now()`, (err,res) => {
//     if(!err){
//         console.log(res.rows)
//     } else{
//         console.log(err.message)
//     }
//     client.end()
// })