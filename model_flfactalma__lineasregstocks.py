# @class_declaration interna_lineasregstocks #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_lineasregstocks(modelos.mtd_lineasregstocks, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_lineasregstocks #
class guanabana_sync_m2_lineasregstocks(interna_lineasregstocks, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineasregstocks #
class lineasregstocks(guanabana_sync_m2_lineasregstocks, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.lineasregstocks_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
