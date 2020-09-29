# @class_declaration interna_tpv_claveacceso #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_claveacceso(modelos.mtd_tpv_claveacceso, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_tpv_claveacceso #
class guanabana_sync_m2_tpv_claveacceso(interna_tpv_claveacceso, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_claveacceso #
class tpv_claveacceso(guanabana_sync_m2_tpv_claveacceso, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_claveacceso_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
