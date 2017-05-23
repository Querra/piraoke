response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Videos'),URL('default','videos_manage')==URL(),URL('default','videos_manage'),[]),
(T('Player'),URL('default','player')==URL(),URL('default','player'),[]),
(T('Favorites'),URL('default','favorites')==URL(),URL('default','favorites'),[]),
(T('Stats'),URL('default','stats')==URL(),URL('default','stats'),[]),
(T('Extra'),URL('default','extra')==URL(),URL('default','extra'),[]),
]