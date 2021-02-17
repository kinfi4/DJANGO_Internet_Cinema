from numba import jit
from mainapp.models import Film


def find_all_similar_films(title: str):
    if not title:
        return None

    title = title.lower()

    words = title.split()
    result = set()

    for film in Film.objects.all():
        if title in film.title:
            result.add(film)
        else:
            title_words = film.title.split()

            for word in words:
                for title_word in title_words:
                    if len(word) > 3:
                        if leven_dist(word, title_word.lower()) < 3:
                            result.add(film)

    return list(result)


@jit
def leven_dist(text1, text2):
    if text1 == '' or text2 == '':
        return len(text2) + len(text1)

    if text1[-1] == text2[-1]:
        return leven_dist(text1[:-1], text2[:-1])

    return min(
        leven_dist(text1[:-1], text2) + 1,
        leven_dist(text1, text2[:-1]) + 1,
        leven_dist(text1[:-1], text2[:-1]) + 1
    )
