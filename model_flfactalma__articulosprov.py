# @class_declaration interna_articulosprov #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_articulosprov(modelos.mtd_articulosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_articulosprov #
class guanabana_sync_m2_articulosprov(interna_articulosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration articulosprov #
class articulosprov(guanabana_sync_m2_articulosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.articulosprov_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
