def average_rating(rating_list: list[int]) -> int:
    """Returns average rating of the books."""

    if not rating_list:
        return 0

    return round(sum(rating_list) / len(rating_list))
