import threading

# Semaphore to synchronize access to the shared resource
semaphore = threading.Semaphore(1)

# Shared resource
sharedResource = 1

def processP1():
    global sharedResource
    for i in range(5):
        # Acquire the semaphore
        semaphore.acquire()
        # Access the shared resource
        sharedResource += 1
        print("\nProcess 1: The shared resource = ", sharedResource)
        # Release the semaphore
        semaphore.release()

def processP2():
    global sharedResource
    for i in range(5):
        # Acquire the semaphore
        semaphore.acquire()
        # Access the shared resource
        sharedResource -= 1
        print("\nProcess 2: The shared resource = ", sharedResource)
        # Release the semaphore
        semaphore.release()


# Creating the processes
proc1 = threading.Thread(target=processP1)
proc2 = threading.Thread(target=processP2)

# Starting the processes
proc1.start()
proc2.start()
