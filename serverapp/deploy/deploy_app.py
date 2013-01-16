#deploy_app.py
from deploy_config import DeployConfiguration


#############################################
#
# deploy aplication, here is where start we
# application deployment proccess.
#
#############################################


class DeployApplication(object):
    deploy_config = DeployConfiguration()

    def __init__(self, app_name):
        self.applocation_name = app_name

    def startApplication():
        pass

    def stopApplication():
        pass

    def destroyApplication():
        pass
