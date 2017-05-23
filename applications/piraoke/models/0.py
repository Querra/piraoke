from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Piraoke'
settings.subtitle = 'powered by web2py'
settings.author = 'Benjamin Quenzer'
settings.author_email = 'b.quenzer@googlemail.com'
settings.keywords = 'pi, karaoke'
settings.description = 'Karaoke application for raspberry pi'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '56f5254c-1be4-4abf-8a5f-132c872ac9a9'
settings.email_server = 'localhost'
settings.email_sender = 'b.quenzer@googlemail.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
