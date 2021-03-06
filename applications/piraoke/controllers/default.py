# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

def index():
    import netifaces as ni
    ni.ifaddresses('eth0')
    ip = ni.ifaddresses('eth0')[2][0]['addr']
    return dict(ip=ip)

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
    volume = request.vars.volume
    if volume is None:
        #set video volume to 90%
        volume = "-662"
    #youtube_url = "https://www.youtube.com/watch?v=1_QZETpgjJw"
    ytdl_command = "omxplayer --vol "+volume+" --aspect-mode stretch $(youtube-dl -g -f 18 'https://www.youtube.com/watch?v="+video_id+"')"
    #dbg.set_trace() # stop here!
    #set microphone volume to 100%
    subprocess.call("amixer cset numid=1 100%", shell=True)
    #start video
    videoProcess = subprocess.Popen(ytdl_command, shell=True)
    video_pid = videoProcess.pid
    #db.t_videos.insert(f_url=video_id, f_pid=video_pid)
    #set microphone volume back to 10% (don't silence completely for testing purposes)
    #subprocess.call("amixer cset numid=1 10%", shell=True)
    return dict()

def cancel():
    #import os
    #import signal

    #video_id = request.vars.video_id
    #rows = db(db.t_videos.f_url == video_id).select()
    #for row in rows:
    #    video_pid = int(row.f_pid)
    #    os.kill(video_pid, signal.SIGTERM)
    import psutil

    PROCNAME = "omxplayer.bin"

    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()
    return dict()

def favorites():
    return dict()

def stats():
    return dict()

def extra():
    return dict()
