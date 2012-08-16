####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.
# In this case, just kick off a 'runtests' build

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.schedulers.forcesched import ForceScheduler
from buildbot.changes import filter

def get_schedulers():
    branch_filter = filter.ChangeFilter(branch='master')

    schedulers = []
    schedulers.append(SingleBranchScheduler(
                          name="all",
                          change_filter=branch_filter,
                          treeStableTimer=None,
                          builderNames=["runtests"]))
    schedulers.append(ForceScheduler(
                          name="force",
                          builderNames=["runtests"]))

    return schedulers
