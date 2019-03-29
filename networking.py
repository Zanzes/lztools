import platform
import queue
import re
import subprocess
import threading

def scan_network(base_ip):
    def worker_func(pingArgs, pending, done):
        try:
            while True:
                # Get the next address to ping.
                address = pending.get_nowait()

                ping = subprocess.Popen(pingArgs + [address],
                                        stdout = subprocess.PIPE,
                                        stderr = subprocess.PIPE
                                        )
                out, error = ping.communicate()

                # Output the result to the 'done' queue.
                done.put((out, error))
        except queue.Empty:
            # No more addresses.
            pass
        finally:
            # Tell the main thread that a worker is about to terminate.
            done.put(None)

    # The number of workers.
    NUM_WORKERS = 256

    plat = platform.system()

    # The arguments for the 'ping', excluding the address.
    if plat == "Windows":
        pingArgs = ["ping", "-n", "1", "-l", "1", "-w", "1000"]
    elif plat == "Linux":
        pingArgs = ["ping", "-c", "1", "-l", "1", "-s", "1", "-W", "1"]
    else:
        raise ValueError("Unknown platform")

    # The queue of addresses to ping.
    pending = queue.Queue()

    # The queue of results.
    done = queue.Queue()

    # Create all the workers.
    workers = []
    for _ in range(NUM_WORKERS):
        workers.append(threading.Thread(target=worker_func, args=(pingArgs, pending, done)))

    # Put all the addresses into the 'pending' queue.
    rmatch = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}", base_ip).group()
    for i in range(2, 257):
        ip = f"{rmatch}.{i}"
        pending.put(ip)

    # Start all the workers.
    for w in workers:
        w.daemon = True
        w.start()

    # Print out the results as they arrive.
    numTerminated = 0
    while numTerminated < NUM_WORKERS:
        result = done.get()
        if result is None:
            # A worker is about to terminate.
            numTerminated += 1
        else:
            r = result[0].decode()
            if "Lost = 0" in r or "1 received" in r:
                m = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", r).group()
                yield m

    # Wait for all the workers to terminate.
    for w in workers:
        w.join()