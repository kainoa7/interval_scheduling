# Interval Scheduling: Greedy Algorithm

This repository contains an implementation of the interval scheduling algorithm using a greedy approach in Python.

## Description

Interval scheduling is a problem in algorithm design and theory that involves scheduling tasks within a given time frame while maximizing the number of tasks that can be completed without conflicts. The goal is to find the maximum number of non-overlapping intervals given a set of intervals, each with a start and finish time.

The greedy algorithm for interval scheduling considers jobs in increasing order of finish time. It takes each job provided it's compatible with the ones already taken. A job is compatible if its start time is greater than or equal to the finish time of the last added job. By sorting the jobs by finish times and selecting compatible jobs greedily, the algorithm efficiently finds the maximum number of non-overlapping intervals.

## Implementation

The provided implementation of the interval scheduling algorithm sorts the jobs by finish times and selects compatible jobs in a greedy manner. Here's the basic outline of the algorithm:

1. Sort jobs by finish times in non-decreasing order.
2. Initialize an empty set of selected jobs.
3. Keep track of the finish time of the last added job.
4. Iterate through the sorted jobs:
   - If the start time of the current job is greater than or equal to the finish time of the last added job, add the job to the selected set and update the last added job's finish time.
5. Return the set of selected jobs.

## How to Use

To use this implementation of the interval scheduling algorithm, follow these steps:

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the Python file.
4. Open a terminal or command prompt.
5. Run the following command to execute the script:

    ```
    python interval_scheduling.py
    ```

6. The script will output the selected jobs, i.e., the maximum number of non-overlapping intervals that can be scheduled.

## Example

Example inputs: jobs = [(1, 3), (2, 5), (3, 6), (6, 8), (7, 10)]
- First number represents start time and second number represents finish time
- Finds maximum subset of mutually compatible jobs.

![interval_schedule](https://github.com/kainoa7/interval_scheduling/assets/97155994/34ca9550-08f8-4b8f-bbd0-05c78e9f218c)


