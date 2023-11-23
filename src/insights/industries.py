from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        if not self.jobs_list:
            return []
        industries = list()
        for job in self.jobs_list:
            industries.append(job['industry'])
        return list(set(industries))
