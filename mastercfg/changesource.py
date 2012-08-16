####### CHANGESOURCES

# the 'change_source' setting tells the buildmaster how it should find out
# about source code changes.  Here we point to the buildbot clone of pyflakes.

from buildbot.changes.gitpoller import GitPoller

def get_change_source():
    change_source = GitPoller(repourl='git://github.com/buildbot/pyflakes.git',
                              workdir='gitpoller-workdir',
                              branch='master',
                              pollinterval=300)

    return change_source
