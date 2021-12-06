"""Test Config class functionality"""


def test_import() -> None:
    """Test dispatcher class import
    """
    from kubot_dispatcher.dispatcher import Dispatcher
    assert type(Dispatcher) == type(type)
