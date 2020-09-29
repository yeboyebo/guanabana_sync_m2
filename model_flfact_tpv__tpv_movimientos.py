# @class_declaration interna_tpv_movimientos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_movimientos(modelos.mtd_tpv_movimientos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_tpv_movimientos #
class guanabana_sync_m2_tpv_movimientos(interna_tpv_movimientos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_movimientos #
class tpv_movimientos(guanabana_sync_m2_tpv_movimientos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_movimientos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
