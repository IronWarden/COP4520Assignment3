import threading
import random

Time = 0 

class MarsRover:
    def __init__(self):
        self.temperatures = [[] for i in range(60)]
        self.lock = threading.Lock()

    def sense_temperature(self):
        global Time
        while Time < 60:  
            temp = round(random.uniform(-100, 70), 2)
            minute = (Time // 60) % 60
            with self.lock:
                self.temperatures[minute].append(temp)
            Time += 1
                
    def compile_report(self):
        global Time
        hour = (Time // 60) % 24
        temps = self.temperatures[(hour - 1) % 60]

        highest_temps = sorted(temps, reverse=True)[:5]
        lowest_temps = sorted(temps)[:5]

        largest_diff = 0
        largest_interval = 0
        for i in range(len(temps) - 10):
            diff = max(temps[i:i+10]) - min(temps[i:i+10])
            if diff > largest_diff:
                largest_diff = diff
                largest_interval = (i, i + 10)

        print(f"Hour {hour} Report:")
        print("Top 5 Highest Temperatures:", highest_temps)
        print("Top 5 Lowest Temperatures:", lowest_temps)
        print("10-Minute Interval with Largest Temperature Difference:",
              largest_interval)


def main():
    threads = []
    num_threads = 8
    rover = MarsRover()

    for i in range(num_threads):
        thread = threading.Thread(target=rover.sense_temperature())
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    rover.compile_report()


if __name__ == "__main__":
    main()
