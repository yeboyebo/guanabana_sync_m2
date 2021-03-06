# @class_declaration interna_tpv_tarjetaspuntos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_tarjetaspuntos(modelos.mtd_tpv_tarjetaspuntos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_tpv_tarjetaspuntos #
class guanabana_sync_m2_tpv_tarjetaspuntos(interna_tpv_tarjetaspuntos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_tarjetaspuntos #
class tpv_tarjetaspuntos(guanabana_sync_m2_tpv_tarjetaspuntos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_tarjetaspuntos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
