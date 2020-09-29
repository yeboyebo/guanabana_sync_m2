# @class_declaration interna_inventarios #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_inventarios(modelos.mtd_inventarios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_inventarios #
class guanabana_sync_m2_inventarios(interna_inventarios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration inventarios #
class inventarios(guanabana_sync_m2_inventarios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.inventarios_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
