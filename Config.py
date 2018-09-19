

class Config(object):
    """
    Base Config class
    """
    pass


class ProdConfig(Config):
    """
    production config class
    """
    pass


class DevConfig(Config):
    """
    development config class
    """
    # Open the Debug
    DEBUG = True
