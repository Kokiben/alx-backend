import { createClient, print } from 'redis';

// Create a Redis client
const client = createClient();

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Store a hash value using hset
const hashKey = 'HolbertonSchools';
client.hset(hashKey, 'Portland', 50, print);
client.hset(hashKey, 'Seattle', 80, print);
client.hset(hashKey, 'New York', 20, print);
client.hset(hashKey, 'Bogota', 20, print);
client.hset(hashKey, 'Cali', 40, print);
client.hset(hashKey, 'Paris', 2, print);

// Retrieve and display the hash value using hgetall
client.hgetall(hashKey, (err, value) => {
  if (err) {
    console.error(`Error retrieving hash ${hashKey}: ${err.message}`);
  } else {
    console.log(value);
  }

  // Close the Redis client connection
  client.quit();
});
