from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salary_list = list()
        for job in self.jobs_list:
            if job["max_salary"].isdigit():
                salary_list.append(int(job["max_salary"]))
        return max(salary_list)

    def get_min_salary(self) -> int:
        salary_list = list()
        for job in self.jobs_list:
            if job["min_salary"].isdigit():
                salary_list.append(int(job["min_salary"]))
        return min(salary_list)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if 'min_salary' not in job or 'max_salary' not in job:
            raise ValueError
        min_salary = job['min_salary']
        max_salary = job['max_salary']
        if type(salary) is not int and type(salary) is not str:
            raise ValueError
        if not str(min_salary).isnumeric() or not str(max_salary).isnumeric():
            raise ValueError
        if (int(min_salary) > int(max_salary)):
            raise ValueError
        return int(min_salary) <= int(salary) <= int(max_salary)

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
