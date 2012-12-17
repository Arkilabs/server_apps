import os


ROOT_APPLICATIONS = os.path.join(os.path.dirname(__file__), '')


class ServerConfig:
    home = ""
    socket = ""
    module = ""
    chmod_socket = ""
    chdir = ""
    virtualenv = ""
    enable_threads = ""
    threads = ""


class ConfigGenerator:

    def __init__(self, application_name):
        self.application_name = application_name

    def generate_config_folder(self):
        self.config_dir = os.path.join(ROOT_APPLICATIONS, "config-" + self.application_name)
        #create config dir for the application
        try:
            if not os.path.exists(self.config_dir):
                os.mkdir(self.config_dir, 0755)
                return True
        except OSError as error:
            print error
        return False

    def generate_config_file(self, type_file):
        if self.generate_config_folder():
            if type_file == "uwsgi":
                config = self.init_config_test()
                file_text = self.create_uwsgi_file(config)
            else:
                return
            wufile = open("%s/%s.ini" % (self.config_dir, self.application_name), "w")
            wufile.write(file_text)
            wufile.close()

    def create_uwsgi_file(self, config):
        file_text = "[uwsgi]\n"
        file_text += "home=%s\n" % config.home
        file_text += "socket=%s\n" % config.socket
        file_text += "chmod-socket=%s\n" % config.chmod_socket
        file_text += "module=%s\n" % config.module
        file_text += "chdir=%s\n" % config.chdir
        file_text += "virtualenv=%s\n" % config.virtualenv
        file_text += "enable-threads=%s\n" % config.enable_threads
        file_text += "threads=%s\n" % config.threads
        return file_text

    def init_config_test(self):
        config = ServerConfig()
        config.home = "/var/apps/garitas_project/"
        config.socket = "/var/sockets/garitas_co.sock"
        config.chmod_socket = "776"
        config.module = "garitas_project.wsgi"
        config.chdir = "/var/apps/garitas_project"
        config.virtualenv = "/var/apps/garitas_project/venv"
        config.enable_threads = "1"
        config.threads = "1"
        return config
