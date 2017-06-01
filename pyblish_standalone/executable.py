import sys
from .vendor.Qt import QtWidgets

import pyblish.api


def start(gui, hosts=[]):
    """ This starts the supplied gui.

    It registers any hosts along with it self "standalone".

    Args:
        gui (module): Module that has a "show" method.
        hosts (list): List of host names to register before starting.
    """

    pyblish.api.register_host("standalone")
    for host in hosts:
        pyblish.api.register_host(host)

    app = QtWidgets.QApplication(sys.argv)
    gui.show()
    sys.exit(app.exec_())


def stop():
    """ Called when shutting down. """
    try:
        import pyblish_aftereffects
        pyblish_aftereffects.stop_server()
    except:
        pass
