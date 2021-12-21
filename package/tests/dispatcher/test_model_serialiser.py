"""Test ModelSerialiser class functionality"""
import pytest

from kubot.exceptions import KubotModelSerialiserError


def test_import() -> None:
    """Test class import
    """
    from kubot.dispatcher import ModelSerialiser
    assert type(ModelSerialiser) == type(type)


def test_init() -> None:
    """Test dispatcher class init
    """
    from kubot.dispatcher import ModelSerialiser
    serialiser = ModelSerialiser(object())
    assert isinstance(serialiser, ModelSerialiser)


def test_value_error() -> None:
    """Test dispatcher class value error
    """
    from kubot.dispatcher import ModelSerialiser
    serialiser = ModelSerialiser(object())
    with pytest.raises(KubotModelSerialiserError):
        serialiser.to_dict()
