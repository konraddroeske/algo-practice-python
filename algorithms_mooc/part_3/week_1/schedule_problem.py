from typing import Union

# Task - Run the greedy algorithm that schedules jobs in decreasing order of the
# different (weight - length)

# If two jobs have equal difference (weight - length), schedule the job with the higher
# weigh first.

# Report the sum of weighted completion times of the resulting schedule -- a positive
# integer.


class JobDifference:
    def __init__(self, weight: int, length: int) -> None:
        self.weight = weight
        self.length = length
        self.diff = self.weight - self.length

    def __repr__(self) -> str:
        return f"JobDifference(Weight: {self.weight}, Length: {self.length}, Diff: {self.diff})"

    def __lt__(self, obj: "JobDifference") -> bool:
        if self.diff == obj.diff:
            return self.weight < obj.weight

        return self.diff < obj.diff

    def __eq__(self, obj: "JobDifference") -> bool:
        return self.diff == obj.diff and self.weight == obj.weight


# job_diff_1 = JobDifference(10, 9)
# job_diff_2 = JobDifference(11, 10)
# job_diff_3 = JobDifference(3, 2)


class JobRatio:
    def __init__(self, weight: int, length: int) -> None:
        self.weight = weight
        self.length = length
        self.ratio = self.weight / self.length

    def __repr__(self) -> str:
        return (
            f"JobRatio(Weight: {self.weight}, Length: {self.length}, "
            f"Ratio: {self.ratio})"
        )

    def __lt__(self, obj: "JobRatio") -> bool:
        return self.ratio < obj.ratio

    def __eq__(self, obj: "JobRatio") -> bool:
        return self.ratio == obj.ratio


# job_ratio_1 = JobRatio(10, 9)
# job_ratio_2 = JobRatio(11, 10)
# job_ratio_3 = JobRatio(3, 2)


def sum_of_weighted_completion_times(jobs: list[Union[JobDifference, JobRatio]]) -> int:
    result = 0
    completion_time = 0

    for job in jobs:
        completion_time += job.length
        result += job.weight * completion_time

    return result


with open("scheduling_input.txt") as f:
    diff_jobs = []
    ratio_jobs = []

    for index, line in enumerate(f):
        split_line = [int(val) for val in str.split(line)]

        if index == 0:
            continue
        else:
            input_weight = split_line[0]
            input_length = split_line[1]

            diff_jobs.append(JobDifference(input_weight, input_length))
            ratio_jobs.append(JobRatio(input_weight, input_length))


sorted_diff_jobs = sorted(diff_jobs, reverse=True)
# print("Sorted diff jobs:", sorted_diff_jobs)

sorted_ratio_jobs = sorted(ratio_jobs, reverse=True)
# print("Sorted ratio jobs:", sorted_ratio_jobs)

part_1 = sum_of_weighted_completion_times(sorted_diff_jobs)
print("Diff Jobs => Sum of weighted completion times:", part_1)

part_2 = sum_of_weighted_completion_times(sorted_ratio_jobs)
print("Ratio Jobs => Sum of weighted completion times:", part_2)
