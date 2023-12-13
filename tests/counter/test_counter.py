from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'

    job_type = count_ocurrences(path, 'job_type')
    industry = count_ocurrences(path, 'industry')

    assert job_type == 1
    assert industry == 1346
