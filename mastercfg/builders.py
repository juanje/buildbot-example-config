####### BUILDSLAVES

# The 'slaves' list defines the set of recognized buildslaves. Each element is
# a BuildSlave object, specifying a unique slave name and password.  The same
# slave name and password must be configured on the slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.shell import ShellCommand
from buildbot.config import BuilderConfig

def build_factory():
    factory = BuildFactory()

    # Step 1: check out the source
    factory.addStep(Git(repourl='git://github.com/buildbot/pyflakes.git',
                        mode='copy'))
    # Step 2: run the tests
    # (note that this will require that 'trial' is installed) 
    factory.addStep(ShellCommand(command=['trial', 'pyflakes']))
    
    return factory

def get_builders():
    builders = []
    builders.append(BuilderConfig(
                        name="runtests",
                        slavenames=["example-slave"],
                        factory=build_factory()))

    return builders

