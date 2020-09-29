# @class_declaration interna_formaspago #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_formaspago(modelos.mtd_formaspago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_formaspago #
class guanabana_sync_m2_formaspago(interna_formaspago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration formaspago #
class formaspago(guanabana_sync_m2_formaspago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.formaspago_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
