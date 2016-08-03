import subprocess, threading, time
import shlex


class Application:
    def __init__(self, app_id, command, agent):
        self.app_id = app_id
        self.command = shlex.split(command)
        self.agent = agent
        self.run_thread = None
        self.p = None

    def start(self):
        print 'Starting:', ' '.join(self.command)
        self.run_thread = threading.Thread(target=self._run_app)
        self.run_thread.daemon = True
        self.run_thread.start()

    def stop(self):
        print 'Stopping ', self.command[0]
        self.p.terminate()
        self.run_thread.join(3)

        if self.run_thread is not None:
            if self.run_thread.is_alive():
                self.p.kill()
                self.run_thread.join()

    def app_stopped(self):
        self.agent.app_stopped(self.app_id)

    def _run_app(self):
        try:
            self.p = subprocess.Popen(self.command)

        except OSError:
            print 'ERROR: %s does not exist!' % self.command[0]

        except ValueError:
            print 'ERROR: Invalid Popen() arguments (programming error)'

        self.agent.app_started(self.app_id)
        self.p.wait()

        # while True:
        #     time.sleep(1)
        #     if not self.p.poll() is None:
        #         break

        self.app_stopped()


class TestServer:
    def app_stopped(self, aid):
        print "stopped:", aid

    def app_started(self, aid):
        print "really started", aid
