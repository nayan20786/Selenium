import pytest
import logging

from LoggingClass import LoggingClass


@pytest.mark.testLog
class TestExample3(LoggingClass):
    def test_IfLoggerWorks(self):
        log = self.getlogger()
        log.info("Some data")
        log.info("Some more data")
        log.info("Some more data to read")
        log.error("oH i CANT ADD MORE DATA")
        log.critical("sike")
