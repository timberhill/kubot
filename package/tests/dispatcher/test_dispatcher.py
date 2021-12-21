"""Test Config class functionality"""


def test_import() -> None:
    """Test dispatcher class import
    """
    from kubot.dispatcher import KubotDispatcher
    assert type(KubotDispatcher) == type(type)
