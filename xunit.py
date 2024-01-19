from test_case import TestCase, TestResult, TestSuite

class WasRun(TestCase):
    def setUp(self):
        self.log = 'setUp '

    def tearDown(self):
        self.log += 'tearDown '

    def test_method(self):
        self.log += 'test_method '

    def test_broken_method(self):
        raise Exception

class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert(test.log == 'setUp test_method tearDown ')

    def test_result(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert(self.result.summary() == '1 run, 0 failed')

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        test.run(self.result)
        assert(self.result.summary() == '1 run, 1 failed')

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert(self.result.summary() == '1 run, 1 failed')

    # TODO: setUpで例外が起こった時もキャッチする p.171

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())

suite = TestSuite()
suite.add(TestCaseTest('test_template_method'))
suite.add(TestCaseTest('test_result'))
suite.add(TestCaseTest('test_failed_result'))
suite.add(TestCaseTest('test_failed_result_formatting'))
suite.add(TestCaseTest('test_suite'))
result = TestResult()
suite.run(result)
print(result.summary())