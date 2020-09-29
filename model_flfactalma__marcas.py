# @class_declaration interna_marcas #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_marcas(modelos.mtd_marcas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_marcas #
class guanabana_sync_m2_marcas(interna_marcas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration marcas #
class marcas(guanabana_sync_m2_marcas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.marcas_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
