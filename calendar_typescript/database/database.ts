//import * as dotenv from 'dotenv'
import dotenv from 'dotenv'
import pg from 'pg'
import * as fs from 'fs';


const { Pool } = pg
dotenv.config()

export const credentials = {
  host: 'localhost',
  user: process.env.POSTGRES_USER,
  port: 5432,
  password: process.env.POSTGRES_PW,
  database: process.env.POSTGRES_DB
}

export default async function createTable () {
  const sql = await fs.promises.readFile('./database.sql', 'utf-8')
  console.log('File data is', sql)
  const pool = new Pool(credentials)
  await pool.connect()
  await pool.query(sql)
  await pool.end()
}


