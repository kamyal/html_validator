#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html
    validation by checking whether every opening tag
    has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    # HINT:
    # use the _extract_tags function below to generate
    # a list of html tags without any extra text;
    # then process these html tags using the balanced
    # parentheses algorithm from the class/book
    # the main difference between your code and the code
    # from class will be that you will have to keep
    # track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags
    stack = []
    tags = _extract_tags(html)
    i = 0
    for tag in tags:
        i = i + 1
        if len(stack) == 0 and i < len(tags):
            stack.append(tag)
        elif i == len(tags) and len(stack) == 0:
            return False
        else:
            if tag.find('/') == -1:
                stack.append(tag)
            else:
                opentag = stack.pop()
                start = opentag.find('<')
                opentag = opentag[start+1: len(opentag)]
                closingtag = tag
                start = closingtag.find('/')
                closingtag = closingtag[start+1: len(closingtag)]
                if opentag != closingtag:
                    return False
                else:
                    return True


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that
    are not meant to be used directly by the user are
    prefixed with an underscore.

    This function returns a list of all the html tags
    contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    end = 0
    start = 0
    while end + 1 < len(html):
        start = html.find("<", end)
        end = html.find(">", start)
        if start != -1 and end != -1:
            tags.append(html[start: end+1])
        else:
            break
            return []
    return tags
