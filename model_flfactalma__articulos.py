# @class_declaration interna_articulos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_articulos(modelos.mtd_articulos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_articulos #
class guanabana_sync_m2_articulos(interna_articulos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration articulos #
class articulos(guanabana_sync_m2_articulos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.articulos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
