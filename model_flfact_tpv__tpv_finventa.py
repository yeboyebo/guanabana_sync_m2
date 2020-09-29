# @class_declaration interna_tpv_finventa #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_finventa(modelos.mtd_tpv_finventa, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_tpv_finventa #
class guanabana_sync_m2_tpv_finventa(interna_tpv_finventa, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_finventa #
class tpv_finventa(guanabana_sync_m2_tpv_finventa, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_finventa_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
