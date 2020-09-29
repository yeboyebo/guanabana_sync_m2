# @class_declaration interna_tpv_anularvales #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_anularvales(modelos.mtd_tpv_anularvales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_tpv_anularvales #
class guanabana_sync_m2_tpv_anularvales(interna_tpv_anularvales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_anularvales #
class tpv_anularvales(guanabana_sync_m2_tpv_anularvales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_anularvales_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
