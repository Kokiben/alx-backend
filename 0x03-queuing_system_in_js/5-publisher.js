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

/**
 * Publishes a message to the channel after a delay
 * @param {string} message - The message to publish
 * @param {number} time - The delay in milliseconds
 */
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
}

// Call publishMessage with the specified arguments
publishMessage('Holberton Student #1 starts', 100);
publishMessage('Holberton Student #2 starts', 200);
publishMessage('KILL_SERVER', 300);
