# @class_declaration interna_clientes #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_clientes(modelos.mtd_clientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_clientes #
class guanabana_sync_m2_clientes(interna_clientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration clientes #
class clientes(guanabana_sync_m2_clientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.clientes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
