# @class_declaration interna_tarifas #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_tarifas(modelos.mtd_tarifas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_tarifas #
class guanabana_sync_m2_tarifas(interna_tarifas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tarifas #
class tarifas(guanabana_sync_m2_tarifas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.tarifas_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
