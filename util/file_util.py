def convert_file_name(original_name: str, replace_char: str = "_", replace_space: bool = True) -> str:
    # Convert characters inhibited for file name.
    converted_name = original_name.replace('\\', replace_char)
    converted_name = converted_name.replace('/', replace_char)
    converted_name = converted_name.replace(':', replace_char)
    converted_name = converted_name.replace('*', replace_char)
    converted_name = converted_name.replace('?', replace_char)
    converted_name = converted_name.replace('"', replace_char)
    converted_name = converted_name.replace('"', replace_char)
    converted_name = converted_name.replace('<', replace_char)
    converted_name = converted_name.replace('>', replace_char)
    converted_name = converted_name.replace('|', replace_char)

    # Replace Space.
    converted_name = converted_name.replace(' ', replace_char)
    converted_name = converted_name.replace('　', replace_char)
    return converted_name
