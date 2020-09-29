# @class_declaration interna_lineasfacturasprov #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_lineasfacturasprov(modelos.mtd_lineasfacturasprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_lineasfacturasprov #
class guanabana_sync_m2_lineasfacturasprov(interna_lineasfacturasprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineasfacturasprov #
class lineasfacturasprov(guanabana_sync_m2_lineasfacturasprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.lineasfacturasprov_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
