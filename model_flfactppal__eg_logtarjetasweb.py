# @class_declaration interna_eg_logtarjetasweb #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_eg_logtarjetasweb(modelos.mtd_eg_logtarjetasweb, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_eg_logtarjetasweb #
class guanabana_sync_m2_eg_logtarjetasweb(interna_eg_logtarjetasweb, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration eg_logtarjetasweb #
class eg_logtarjetasweb(guanabana_sync_m2_eg_logtarjetasweb, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.eg_logtarjetasweb_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
