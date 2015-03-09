from checkio_referee import RefereeBase
from checkio_referee.rank import RefereeRank

import settings
import settings_env
from tests import TESTS

cover = """def cover(func, data):
    return func([str(row) for row in data])
"""


class Referee(RefereeRank):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "referee"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": None,
        "javascript": None
    }
