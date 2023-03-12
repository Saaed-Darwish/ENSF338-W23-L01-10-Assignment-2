import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        # acquire lock
        self.lock()

        # check if queue is full
        if (self.tail + 1) % self.size == self.head:
            print("Queue is full, waiting...")
            # release lock and wait for one second before trying again
            self.unlock()
            time.sleep(1)
            self.enqueue(data)
        else:
            # insert data at tail
            if self.head == -1:
                self.head = 0
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = data
            print(f"Enqueued {data}")

            # release lock
            self.unlock()

    def dequeue(self):
        # acquire lock
        self.lock()

        # check if queue is empty
        if self.head == -1:
            print("Queue is empty, waiting...")
            # release lock and wait for one second before trying again
            self.unlock()
            time.sleep(1)
            return self.dequeue()
        else:
            # retrieve data at head
            data = self.queue[self.head]
            print(f"Dequeued {data}")
            
            # update head
            if self.head == self.tail:
                self.head = self.tail = -1
            else:
                self.head = (self.head + 1) % self.size

            # release lock
            self.unlock()

            # return dequeued data
            return data

def producer():
    while True:
        random_number = random.randint(1, 10)
        time.sleep(random_number)
        q.enqueue(random_number)

def consumer():
    while True:
        random_number = random.randint(1, 10)
        time.sleep(random_number)
        dequeued_number = q.dequeue()
        print(dequeued_number)

if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
