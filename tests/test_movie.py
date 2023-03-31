import pytest
from viewing_party.movie import Movie
def test_creating_movie_initializes_instance_variables():
    # Arrange / Act
    frozen = Movie("frozen", "children", 4)

    # Assert
    assert frozen.name == "frozen"
    assert frozen.genre == "children"
    assert frozen.rating == 4