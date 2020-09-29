# @class_declaration interna_pedidoscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_pedidoscli(modelos.mtd_pedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_pedidoscli #
class guanabana_sync_m2_pedidoscli(interna_pedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration pedidoscli #
class pedidoscli(guanabana_sync_m2_pedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.pedidoscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
