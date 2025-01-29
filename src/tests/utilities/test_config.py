import pytest

from designpatterns.utilities.config import load_config


class TestConfig:
    def test__load_config__value_error(self) -> None:
        with pytest.raises(ValueError, match='Section sql not found in the database.ini file') as e:
            load_config(filename='database.ini', section='sql')
        assert e.type is ValueError
