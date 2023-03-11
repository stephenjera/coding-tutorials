import * as dotenv from 'dotenv'
import pg from 'pg'
import { readFile } from 'fs/promises'

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
  const sql = await readFile('./database/init.sql', 'utf-8')
  console.log('File data is', sql)
  const pool = new Pool(credentials)
  await pool.connect()
  await pool.query(sql)
  await pool.end()
}

// module.exports = createTable
// ;(async () => {
//   const clientResult = await createTable()
//   console.log('Time with client: ' + clientResult /*.rows[0]['now']*/)
// })()

