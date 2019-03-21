from third.DockerData import DockerData
from core.lztools import command

def get_running():
    res = command("sudo", "docker", "ps", "-a", u"--format '{{.ID}}*{{.Image}}*{{.Command}}*{{.CreatedAt}}*{{.RunningFor}}*{{.Ports}}*{{.Status}}*{{.Size}}*{{.Names}}*{{.Labels}}*{{.Mounts}}*{{.Networks}}'", return_result=True)

    for d in res[1].splitlines():
        yield DockerData(d, delimiter="*")

def cleanup():
    command("sudo docker container rm $(sudo docker container ls -a --format=\"{{.Names}}\")")
    command("sudo docker container prune -af")
    command("sudo docker image rm $(sudo docker image ls -a --format=\"{{.ID}}\")")
    command("sudo docker image prune -af")