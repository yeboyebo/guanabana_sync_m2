# @class_declaration interna_plantillastextofac #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_plantillastextofac(modelos.mtd_plantillastextofac, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_plantillastextofac #
class guanabana_sync_m2_plantillastextofac(interna_plantillastextofac, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration plantillastextofac #
class plantillastextofac(guanabana_sync_m2_plantillastextofac, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.plantillastextofac_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
