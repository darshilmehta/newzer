from django import template

register = template.Library()

def authorlist_to_string(lst):
    if len(lst) == 1:
        return lst[-1]
    
    author_str = ""
    for i in range(len(lst)-1):
        author_str = author_str + str(lst[i]) + ", "
    author_str = author_str + lst[-1]
    return author_str

register.filter('authorlist_to_string', authorlist_to_string)