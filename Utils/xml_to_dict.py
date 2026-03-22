import xmltodict


def get_ispring_only_quiz(s: str) -> list[dict]:
    out_list = []
    my_dict = xmltodict.parse(s)
    contents_ispring: list = my_dict.get('response').get('contentItem')
    for content in contents_ispring:
        if content.get('contentItemType') == 'Quiz':
            out_list.append(content)
    return out_list


def get_ispring_enrollments(s: str) -> list[dict]:
    my_dict = xmltodict.parse(s)
    enrollments_ispring = my_dict.get('response').get('enrollment')
    if type(enrollments_ispring) is dict:
        return [enrollments_ispring, ]
    return enrollments_ispring


def get_ispring_contents(s: str) -> list[dict]:
    my_dict = xmltodict.parse(s)
    contents_ispring: list = my_dict.get('response').get('contentItem')
    return contents_ispring
