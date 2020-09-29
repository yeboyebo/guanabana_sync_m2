# @class_declaration interna_impuestos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_impuestos(modelos.mtd_impuestos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_impuestos #
class guanabana_sync_m2_impuestos(interna_impuestos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration impuestos #
class impuestos(guanabana_sync_m2_impuestos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.impuestos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
