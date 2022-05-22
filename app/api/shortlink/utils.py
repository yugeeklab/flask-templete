def load_data(short_link_obj):
    """ Load user's data
    Parameters:
    - User db object
    """
    from .schema import ShortLinkSchema

    short_link_schema = ShortLinkSchema()

    data = short_link_schema.dump(short_link_obj)

    return data