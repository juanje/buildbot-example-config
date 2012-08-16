from buildbot.status import html
from buildbot.status.web import authz, auth

def get_status():
    authz_cfg = authz.Authz(
        auth = auth.BasicAuth([("pyflakes", "pyflakes")]),
        gracefulShutdown = False,
        forceBuild = 'auth',
        forceAllBuilds = False,
        pingBuilder = False,
        stopBuild = False,
        stopAllBuilds = False,
        cancelPendingBuild = False,
    )

    status = []
    status.append(html.WebStatus(http_port=8010, authz=authz_cfg))

    return status
