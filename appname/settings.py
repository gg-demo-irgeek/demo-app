import tempfile

db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = "eephee6joot0zu5nao4Uo3aiR9eoc8Ee2Aim0aith1bie3Quael2keelo8uu"


class ProdConfig(Config):
    SERVER_NAME = "replace me"
    ENV = "prod"
    SQLALCHEMY_DATABASE_URI = "sqlite:///../database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CACHE_TYPE = "simple"


class DevConfig(Config):
    SERVER_NAME = "localhost:5000"
    ENV = "dev"
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = "sqlite:///../database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CACHE_TYPE = "null"
    ASSETS_DEBUG = True


class TestConfig(Config):
    SERVER_NAME = "localhost:5000"
    ENV = "test"
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + db_file.name
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CACHE_TYPE = "null"
    WTF_CSRF_ENABLED = False
