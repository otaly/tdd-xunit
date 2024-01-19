class TestResult:
    def __init__(self) -> None:
        self.run_count = 0
        self.error_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.error_count += 1

    def summary(self) -> str:
        return f'{self.run_count} run, {self.error_count} failed'

class TestCase:
    def __init__(self, name: str) -> None:
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, result: TestResult) -> None:
        result.test_started()

        self.setUp()
        method = getattr(self, self.name)

        try:
            method()
        except:
            result.test_failed()

        self.tearDown()

class TestSuite:
    def __init__(self) -> None:
        self.tests: list[TestCase] = []

    def add(self, test: TestCase):
        self.tests.append(test)

    def run(self, result: TestResult) -> None:
        for test in self.tests:
            test.run(result)