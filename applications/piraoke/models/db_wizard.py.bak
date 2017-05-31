### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_videos',
    Field('f_title', type='string',
          label=T('Title')),
    Field('f_url', type='string',
          label=T('Url')),
    Field('f_youtube_url', type='string',
          label=T('Youtube Url')),
    Field('f_length', type='string',
          label=T('Length')),
    Field('f_display_image_url', type='string',
          label=T('Display Image Url')),
    Field('f_artist', type='string',
          label=T('Artist')),
    Field('f_last_viewed', type='string',
          label=T('Last Viewed')),
    Field('f_active', type='string',
          label=T('Active')),
    Field('f_times_played', type='string',
          label=T('Times Played')),
    Field('f_favorite', type='string',
          label=T('Favorite')),
    Field('f_category', type='string',
          label=T('Category')),
    auth.signature,
    format='%(f_title)s',
    migrate=settings.migrate)

db.define_table('t_videos_archive',db.t_videos,Field('current_record','reference t_videos',readable=False,writable=False))
