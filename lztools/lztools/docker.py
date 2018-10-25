from lztools.lztools import command
from lztools.DockerData import DockerData

def get_running():
    res = command("sudo", "docker", "ps", "-a", u"--format '{{.ID}}*{{.Image}}*{{.Command}}*{{.CreatedAt}}*{{.RunningFor}}*{{.Ports}}*{{.Status}}*{{.Size}}*{{.Names}}*{{.Labels}}*{{.Mounts}}*{{.Networks}}'", return_result=True)

    for d in res[1].splitlines():
        yield DockerData(d, delimiter="*")
