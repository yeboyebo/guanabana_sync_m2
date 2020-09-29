# @class_declaration interna_lineaspedidoscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_lineaspedidoscli(modelos.mtd_lineaspedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_lineaspedidoscli #
class guanabana_sync_m2_lineaspedidoscli(interna_lineaspedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineaspedidoscli #
class lineaspedidoscli(guanabana_sync_m2_lineaspedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.lineaspedidoscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
