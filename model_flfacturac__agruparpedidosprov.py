# @class_declaration interna_agruparpedidosprov #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_agruparpedidosprov(modelos.mtd_agruparpedidosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_agruparpedidosprov #
class guanabana_sync_m2_agruparpedidosprov(interna_agruparpedidosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration agruparpedidosprov #
class agruparpedidosprov(guanabana_sync_m2_agruparpedidosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.agruparpedidosprov_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
