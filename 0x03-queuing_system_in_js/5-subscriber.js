import { createClient } from 'redis';

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

// Subscribe to the channel 'holberton school channel'
const channel = 'holberton school channel';
client.subscribe(channel);

// Handle incoming messages
client.on('message', (ch, message) => {
  console.log(`Received message: ${message}`);

  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  }
});
