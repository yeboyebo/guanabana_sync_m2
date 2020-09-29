# @class_declaration interna_lineaspedidosprov #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_lineaspedidosprov(modelos.mtd_lineaspedidosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_lineaspedidosprov #
class guanabana_sync_m2_lineaspedidosprov(interna_lineaspedidosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineaspedidosprov #
class lineaspedidosprov(guanabana_sync_m2_lineaspedidosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.lineaspedidosprov_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
