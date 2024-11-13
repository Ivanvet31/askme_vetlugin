def paginations_params(page_num, paginator, page):
    two_pages_ahead = page_num + 2
    two_pages_behind = page_num - 2

    try:
        arrows_left_border = paginator.page(two_pages_behind)
        left_switch = True
    except (IndexError, ValueError):
        left_switch = False
        arrows_left_border = None

    try:
        arrows_right_border = paginator.page(two_pages_ahead)
        right_switch = True
    except (IndexError, ValueError):
        right_switch = False
        arrows_right_border = None

    is_first_page = True if page.number == 1 else False
    is_last_page = True if page.number == len(paginator.page_range) else False

    params = {
        'left_switch': left_switch,
        'right_switch': right_switch,
        'is_first_page': is_first_page,
        'is_last_page': is_last_page,
        'arrows_left_border': arrows_left_border,
        'arrows_right_border': arrows_right_border,
        'two_pages_ahead': two_pages_ahead,
        'two_pages_behind': two_pages_behind,
    }

    return params
