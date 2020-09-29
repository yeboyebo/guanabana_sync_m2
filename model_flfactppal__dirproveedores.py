# @class_declaration interna_dirproveedores #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_dirproveedores(modelos.mtd_dirproveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_dirproveedores #
class guanabana_sync_m2_dirproveedores(interna_dirproveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration dirproveedores #
class dirproveedores(guanabana_sync_m2_dirproveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.dirproveedores_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
