# Problem URL: https://www.geeksforgeeks.org/job-sequencing-problem/


#User function Template for python3

class Job:
    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

class Solution:
    
    def JobScheduling(self, Jobs, n):
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        max_deadline = max(job.deadline for job in Jobs)
        slots = [-1] * (max_deadline + 1)
        total_profit = 0
        num_jobs = 0
        
        for job in Jobs:
            for slot in range(job.deadline, 0, -1):
                if slots[slot] == -1:
                    slots[slot] = job.id
                    total_profit += job.profit
                    num_jobs += 1
                    break
        
        return [num_jobs, total_profit]



if __name__ == "__main__":
    jobs = [Job(100, 2), Job(19, 1), Job(27, 2), Job(25, 1), Job(15, 3)]
    solution = Solution()
    result = solution.JobScheduling(jobs, len(jobs))
    print("Number of jobs done:", result[0])
    print("Total profit:", result[1])
