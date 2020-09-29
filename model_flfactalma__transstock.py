# @class_declaration interna_transstock #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_transstock(modelos.mtd_transstock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_transstock #
class guanabana_sync_m2_transstock(interna_transstock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration transstock #
class transstock(guanabana_sync_m2_transstock, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.transstock_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
