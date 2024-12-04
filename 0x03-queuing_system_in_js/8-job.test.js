import kue from 'kue';
import createPushNotificationsJobs from '../8-job';  // Adjust path as needed
import { expect } from 'chai';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode = true;  // Enable test mode
  });

  afterEach(() => {
    queue.testMode = false; // Disable test mode
    queue.removeCompleted(); // Clear the queue
  });

  it('should add jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Message 1' },
      { phoneNumber: '4153518781', message: 'Message 2' }
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobIds = queue.testMode.jobs.map(job => job.id);
    expect(jobIds).to.have.lengthOf(2);
  });

  it('should throw error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should log job creation', (done) => {
    const jobs = [{ phoneNumber: '4153518780', message: 'Message 1' }];
    const logSpy = sinon.spy(console, 'log');

    createPushNotificationsJobs(jobs, queue);

    setTimeout(() => {
      expect(logSpy.calledWithMatch(/Notification job created/)).to.be.true;
      logSpy.restore();
      done();
    }, 100);
  });
});
