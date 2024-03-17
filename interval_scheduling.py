def interval_scheduling(jobs):
    # Sort jobs by finish times
    sorted_jobs = sorted(jobs, key=lambda x: x[1])
    
    # Empty set for selected jobs
    selected_jobs = []
    
    # Tracks finish time of the last added job
    last_added_job_finish_time = float('-inf')
    
    # Iterate through sorted jobs
    for job in sorted_jobs:
        start_time, finish_time = job
        
        # If job does not overlap with the last added job
        if start_time >= last_added_job_finish_time:
            selected_jobs.append(job)
            last_added_job_finish_time = finish_time
    
    return selected_jobs

# Example inputs
jobs = [(1, 3), (2, 5), (3, 6), (6, 8), (7, 10)]
selected_jobs = interval_scheduling(jobs)
print("Selected Jobs:", selected_jobs)