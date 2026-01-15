import random

BUZZ_WORDS = (
    "continuous testing",
    "continuous integration",
    "continuous deployment",
    "continuous improvement",
    "devops",
)

ADJECTIVES = (
    "complete",
    "modern",
    "self-service",
    "integrated",
    "end-to-end",
)

ADVERBS = (
    "remarkably",
    "enormously",
    "substantially",
    "significantly",
    "seriously",
)

VERBS = (
    "accelerates",
    "improves",
    "enhances",
    "revamps",
    "boosts",
)


def sample(items, n=1):
    """Return n willekeurige items uit een tuple/lijst."""
    result = random.sample(items, n)
    if n == 1:
        return result[0]
    return result


def generate_buzz():
    buzz_terms = sample(BUZZ_WORDS, 2)
    phrase = " ".join(
        [
            sample(ADJECTIVES),
            buzz_terms[0],
            sample(ADVERBS),
            sample(VERBS),
            buzz_terms[1],
        ]
    )
    return phrase.title()
