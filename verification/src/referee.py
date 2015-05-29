from checkio_referee import RefereeRank


import settings_env
from tests import TESTS

cover = """def cover(func, data):
    return func([str(row) for row in data])
"""


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "xo_referee"
    ENV_COVERCODE = {
        "python_3": None,
        "javascript": None
    }


