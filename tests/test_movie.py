import pytest
from viewing_party.movie import Movie


def test_creating_person_initializes_instance_variables():
    # Arrange / Act
    frozen = Movie("Frozen","children", 4)

    # Assert
    assert frozen.name == "Frozen"
    assert frozen.genre == "children"
    assert frozen.rating == 4

def test_1():
    # Arrange

    # Act

    # Assert
    pass