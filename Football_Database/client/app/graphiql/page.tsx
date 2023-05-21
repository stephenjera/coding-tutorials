import Image from 'next/image'

function Home () {
  return (
    <div className='flex flex-col items-center justify-center'>
      <div className='w-32 h-32 relative'>
        <Image
          src='https://www.pngfind.com/pngs/m/62-627254_i-wanted-to-give-graphql-a-shot-for.png'
          layout='fill'
          objectFit='contain'
          alt='GraphQL Logo'
        />
      </div>
      <button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded'>
        {' '}
        <a href='http://localhost:3001/graphql' target='blank'>
          Try my API
        </a>
      </button>
    </div>
  )
}

export default Home
