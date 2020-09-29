# @class_declaration interna_almacenes #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_almacenes(modelos.mtd_almacenes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_almacenes #
class guanabana_sync_m2_almacenes(interna_almacenes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration almacenes #
class almacenes(guanabana_sync_m2_almacenes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.almacenes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
