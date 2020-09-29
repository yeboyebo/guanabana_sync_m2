# @class_declaration interna_series #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_series(modelos.mtd_series, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_series #
class guanabana_sync_m2_series(interna_series, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration series #
class series(guanabana_sync_m2_series, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.series_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
