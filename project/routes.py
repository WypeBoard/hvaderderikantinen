def includeme(config):
    """
    Defines all endpoints in the application

    Making a new endpoint needs to be defined in this method
    """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
