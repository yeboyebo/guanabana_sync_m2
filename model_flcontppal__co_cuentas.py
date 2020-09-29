# @class_declaration interna_co_cuentas #
import importlib

from YBUTILS.viewREST import helpers

from models.flcontppal import models as modelos


class interna_co_cuentas(modelos.mtd_co_cuentas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_co_cuentas #
class guanabana_sync_m2_co_cuentas(interna_co_cuentas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration co_cuentas #
class co_cuentas(guanabana_sync_m2_co_cuentas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcontppal.co_cuentas_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
