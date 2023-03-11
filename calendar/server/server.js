// server/index.js
//const express = require('express')
import express from 'express'
import * as dotenv from 'dotenv'
import pg from 'pg'
import { readFile } from 'fs/promises'

const PORT = process.env.PORT || 3001
const app = express()
const { Client } = pg
dotenv.config()

const credentials = {
  host: 'localhost',
  user: process.env.POSTGRES_USER,
  port: 5432,
  password: process.env.POSTGRES_PW,
  database: process.env.POSTGRES_DB
}

async function createTable () {
  const sql = await readFile('./database/init.sql', 'utf-8')
  console.log('File data is', sql)
  const client = new Client(credentials)
  await client.connect()
  await client.query(sql)
  await client.end()

}

;(async () => {
  const clientResult = await createTable()
  console.log('Time with client: ' + clientResult/*.rows[0]['now']*/)
})()

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`)
})
