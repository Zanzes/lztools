from platform import system,uname

Linux = "Linux"
Windows = "Windows"
WSL = "WSL"
Cygwin = "Cygwin"
Mac = "Mac"
Bsd = "Bsd"

def identify():
    syst = system().lower()
    if 'cygwin' in syst:
        return Cygwin
    elif 'darwin' in syst:
        return Mac
    elif 'linux' in syst:
        if 'Microsoft' not in uname().release:
            return Linux
        return WSL
    elif 'windows' in syst:
        return Windows
    elif 'bsd' in syst:
        return Bsd

print(identify())