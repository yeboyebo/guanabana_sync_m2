# @class_declaration interna_articulostarifas #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_articulostarifas(modelos.mtd_articulostarifas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_articulostarifas #
class guanabana_sync_m2_articulostarifas(interna_articulostarifas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration articulostarifas #
class articulostarifas(guanabana_sync_m2_articulostarifas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.articulostarifas_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
