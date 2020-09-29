# @class_declaration interna_lineasfacturascli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_lineasfacturascli(modelos.mtd_lineasfacturascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_lineasfacturascli #
class guanabana_sync_m2_lineasfacturascli(interna_lineasfacturascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineasfacturascli #
class lineasfacturascli(guanabana_sync_m2_lineasfacturascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.lineasfacturascli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
