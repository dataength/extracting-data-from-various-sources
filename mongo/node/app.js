const { MongoClient } = require('mongodb')

const username = 'dataength'
const password = 'xyz'
const hostName = 'cluster0.xyz.mongodb.net'
const dbName = 'sample_airbnb'
const collectionName = 'listingsAndReviews'

const run = async () => {
  const uri = `mongodb+srv://${username}:${password}@${hostName}/${dbName}?retryWrites=true&w=majority`
  const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true })
  await client.connect()

  const collection = client.db(dbName).collection(collectionName)

  const query = {}
  const options = {}
  const cursor = collection.find(query, options)

  if ((await cursor.count()) === 0) {
    console.log('No documents found!');
  }

  await cursor.forEach(result => {
    console.log(result)
  })

  await client.close()
}

run()
