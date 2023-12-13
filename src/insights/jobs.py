from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, msg) -> List[Dict]:
        with open(msg, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.jobs_list.append(row)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        if not self.jobs_list:
            return []
        job_types = list()
        for job in self.jobs_list:
            job_types.append(job['job_type'])
        return list(set(job_types))

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
