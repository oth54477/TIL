def solution(today, terms, privacies):
    def make_day_to_row(y, m, d):
        return y * (28 * 12) + m * 28 + d
    
    terms_dict = dict()
    for term in terms:
        key, value = term.split()
        terms_dict[key] = int(value)

    y, m, d = map(int, today.split("."))
    today_row = make_day_to_row(y, m, d)

    result = []
    for idx, privacy in enumerate(privacies):
        day, case = privacy.split()
        y, m, d = map(int, day.split("."))
        case_value = terms_dict[case]
        privacy_row = make_day_to_row(y, m+case_value, d)
        if privacy_row <= today_row:
            result.append(idx + 1)

    return result