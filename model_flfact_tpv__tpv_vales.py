# @class_declaration interna_tpv_vales #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_vales(modelos.mtd_tpv_vales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_tpv_vales #
class guanabana_sync_m2_tpv_vales(interna_tpv_vales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_vales #
class tpv_vales(guanabana_sync_m2_tpv_vales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_vales_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
