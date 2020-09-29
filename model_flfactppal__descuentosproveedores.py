# @class_declaration interna_descuentosproveedores #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_descuentosproveedores(modelos.mtd_descuentosproveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_descuentosproveedores #
class guanabana_sync_m2_descuentosproveedores(interna_descuentosproveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration descuentosproveedores #
class descuentosproveedores(guanabana_sync_m2_descuentosproveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.descuentosproveedores_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
