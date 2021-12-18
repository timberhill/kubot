"""Test Config class functionality"""


def test_import() -> None:
    """Test dispatcher class import
    """
    from kubot.dispatcher import Dispatcher
    assert type(Dispatcher) == type(type)
