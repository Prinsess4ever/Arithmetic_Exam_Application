from hstest import StageTest, TestedProgram, CheckResult, dynamic_test


class ExamTest(StageTest):
    @dynamic_test
    def test_sum(self):
        pr = TestedProgram()
        pr.start()
        output = pr.execute("5 + 2").lower().strip()
        check = output == "7" or output == "7.0"
        return CheckResult(check, 'Wrong result found for "+" operation.')

    @dynamic_test
    def test_mult(self):
        pr = TestedProgram()
        pr.start()
        output = pr.execute("11 * 3").lower().strip()
        check = output == "33" or output == "33.0"
        return CheckResult(check, 'Wrong result found for "*" operation.')

    @dynamic_test
    def test_substraction(self):
        pr = TestedProgram()
        pr.start()
        output = pr.execute("10 - 3").lower().strip()
        check = output == "7" or output == "7.0"
        return CheckResult(check, 'Wrong result found for "-" operation.')


if __name__ == '__main__':
    ExamTest().run_tests()
