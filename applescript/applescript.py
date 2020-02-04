from subprocess import Popen, PIPE


def run(script: str) -> str:
    """
    Returns the result of running string in osascript (Applescript)
    """
    osa = Popen(["osascript", "-"], stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding="utf-8")
    results, err = osa.communicate(script)
    return results



