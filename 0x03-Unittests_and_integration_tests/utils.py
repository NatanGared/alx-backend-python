def access_nested_map(nested_map, path):
    try:
        for key in path:
            nested_map = nested_map[key]
        return nested_map
    except (KeyError, TypeError):
        return None