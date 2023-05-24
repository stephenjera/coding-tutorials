import type { NextApiRequest, NextApiResponse } from 'next'


interface User {
  id: number;
}

// Fake users data
const users: User[] = [{id:1},{id:2},{id:3}]

export default function handler(req: NextApiRequest, res: NextApiResponse<User[]>){
  // Get data from your database
  res.status(200).json(users)
}
