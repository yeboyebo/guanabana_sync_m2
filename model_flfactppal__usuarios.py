# @class_declaration interna_usuarios #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_usuarios(modelos.mtd_usuarios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_usuarios #
class guanabana_sync_m2_usuarios(interna_usuarios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration usuarios #
class usuarios(guanabana_sync_m2_usuarios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.usuarios_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
