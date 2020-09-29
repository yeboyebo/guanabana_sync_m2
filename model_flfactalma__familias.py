# @class_declaration interna_familias #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_familias(modelos.mtd_familias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_familias #
class guanabana_sync_m2_familias(interna_familias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration familias #
class familias(guanabana_sync_m2_familias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.familias_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
