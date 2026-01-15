import os
import sys

# Voeg de project-root (cicd-buzz) toe aan sys.path,
# zodat 'buzz' als package gevonden wordt.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from buzz.generator import generate_buzz, BUZZ_WORDS


def test_generate_buzz_returns_string():
    phrase = generate_buzz()
    assert isinstance(phrase, str)
    assert len(phrase) > 0


def test_generate_buzz_contains_known_word():
    phrase = generate_buzz().lower()
    assert any(word in phrase for word in BUZZ_WORDS)
