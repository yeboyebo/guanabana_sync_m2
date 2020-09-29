# @class_declaration interna_tpv_tarjetaspago #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_tarjetaspago(modelos.mtd_tpv_tarjetaspago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_tpv_tarjetaspago #
class guanabana_sync_m2_tpv_tarjetaspago(interna_tpv_tarjetaspago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_tarjetaspago #
class tpv_tarjetaspago(guanabana_sync_m2_tpv_tarjetaspago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_tarjetaspago_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
