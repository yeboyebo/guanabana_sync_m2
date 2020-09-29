# @class_declaration interna_presupuestoscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_presupuestoscli(modelos.mtd_presupuestoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_presupuestoscli #
class guanabana_sync_m2_presupuestoscli(interna_presupuestoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration presupuestoscli #
class presupuestoscli(guanabana_sync_m2_presupuestoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.presupuestoscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
