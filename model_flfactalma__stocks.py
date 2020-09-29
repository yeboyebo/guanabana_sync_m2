# @class_declaration interna_stocks #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_stocks(modelos.mtd_stocks, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_stocks #
class guanabana_sync_m2_stocks(interna_stocks, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration stocks #
class stocks(guanabana_sync_m2_stocks, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.stocks_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
