# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

def index():
    return dict()

def error():
    return dict()

def videos_manage():
    form = SQLFORM.smartgrid(db.t_videos,onupdate=auth.archive)
    return locals()

def player():
    import subprocess
    from gluon.debug import dbg
    video_id = request.vars.video_id
    if video_id is None:
        raise HTTP(422,"video_id is not defined")
    #youtube_url = "https://www.youtube.com/watch?v=1_QZETpgjJw"
    ytdl_command = "omxplayer --vol -3000 --aspect-mode stretch $(youtube-dl -g -f 18 'https://www.youtube.com/watch?v="+video_id+"')"
    #dbg.set_trace() # stop here!
    subprocess.call(ytdl_command, shell=True)
    #return response.json(['process', {'pid': }])
    return dict()

def favorites():
    return dict()

def stats():
    return dict()

def extra():
    return dict()
