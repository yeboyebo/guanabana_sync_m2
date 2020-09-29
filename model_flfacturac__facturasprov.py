# @class_declaration interna_facturasprov #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_facturasprov(modelos.mtd_facturasprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_facturasprov #
class guanabana_sync_m2_facturasprov(interna_facturasprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration facturasprov #
class facturasprov(guanabana_sync_m2_facturasprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.facturasprov_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
