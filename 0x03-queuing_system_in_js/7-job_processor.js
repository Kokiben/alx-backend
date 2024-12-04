import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Array containing blacklisted phone numbers
const blacklistedNumbers = [
  '4153518780',
  '4153518781'
];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // Track progress of the job
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    job.fail(errorMessage);  // Fail the job with the error message
    console.log(errorMessage);
    return done(new Error(errorMessage));  // Call done with error
  }

  // Otherwise, process the job
  job.progress(50, 100);  // Track progress to 50%

  // Log sending notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Track job completion
  job.progress(100, 100);  // Track progress to 100%
  done();  // Indicate job is done
}

// Process jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  // Get phone number and message from job data
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function
  sendNotification(phoneNumber, message, job, done);
})
