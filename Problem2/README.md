# How to Run

Have the latest python3 version
python3 Problem1.py

# Proof of correctness

I have used locks and I believe that to be a good approach if each sensor can retrieve and record temperature data fast. I don't think a lock-free approach exists here as all sensors will finish at roughly the same time. I initially planned to use a semaphore but having multiple threads to enter the critical section doesn't seem like the correct approach in this problem either.

# Efficiency

Althought contention is a problem as every thread will finish and want to access the data at the same time, I believe a lock is still preferable since all we are doing is writing in the data to a shared memory.

# Experimental Evaluation

I have tested this program many times tweaking the time parameters. I decided to not go for an infinite loop which I initially had and just stop after the first hour passes.
