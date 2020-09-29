# @class_declaration interna_agentes #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_agentes(modelos.mtd_agentes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_agentes #
class guanabana_sync_m2_agentes(interna_agentes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration agentes #
class agentes(guanabana_sync_m2_agentes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.agentes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
