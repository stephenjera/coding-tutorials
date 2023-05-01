import { useQuery } from '@apollo/client'
import gql from 'graphql-tag'

const MY_QUERY = gql`
  query {
    clubs {
      club
      clubId
    }
  }
`

export default function Clubs () {
  const { loading, error, data } = useQuery(MY_QUERY)

  if (loading) return <p>Loading...</p>
  if (error) return <p>Error :(</p>

  return (
    <ul>
      {data.clubs.map(club => (
        <li key={club.clubId}>{club.club}</li>
      ))}
    </ul>
  )
}
