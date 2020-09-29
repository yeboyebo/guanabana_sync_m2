# @class_declaration interna_factalma_general #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_factalma_general(modelos.mtd_factalma_general, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_factalma_general #
class guanabana_sync_m2_factalma_general(interna_factalma_general, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration factalma_general #
class factalma_general(guanabana_sync_m2_factalma_general, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.factalma_general_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
