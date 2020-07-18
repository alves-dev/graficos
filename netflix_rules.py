def type_graphic_valid(type_graphic: str) -> bool:
    if isinstance(type_graphic, str):
        if valid_type_graphic(type_graphic):
            return True
        return False
    return False


def valid_type_graphic(type_graphic: str) -> bool:
    if type_graphic == 'compare' or type_graphic == 'bars':
        return True
    return False


def valid_archive_upload(archive: str) -> bool:
    if '.csv' in archive:
        return True
    return False
