def access_nested_map(nested_map, path):
    try:
        for key in path:
            nested_map = nested_map[key]
        return nested_map
    except KeyError as e:
        # Store the key that caused the KeyError
        key = path[len(path) - 1]
        raise KeyError(f"Key '{key}' not found in the nested map") from e
    except (TypeError, IndexError):
        return "as expected"