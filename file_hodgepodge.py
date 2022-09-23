from typing import List

def grep(pattern: str, file: str) -> List[str]:
    
    search_strings = []
    
    file = open(file, 'r')
    copy_file = file.read().split('\n')
    file.close()
    
    for _string_ in copy_file:
        if pattern in _string_:
            search_strings.append(_string_)
    
    return search_strings