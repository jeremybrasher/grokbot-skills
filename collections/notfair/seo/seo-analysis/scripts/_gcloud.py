"""Helpers for invoking the gcloud CLI portably."""

import shutil
import subprocess
import sys


def gcloud_command(args):
    """Return a subprocess argument list for a gcloud command.

    On Windows, the Google Cloud SDK installs gcloud as gcloud.cmd. Python's
    shell=False path resolution does not expand PATHEXT for CreateProcess, so
    invoke the resolved batch file through cmd.exe.
    """
    if not args or args[0] != "gcloud":
        raise ValueError("gcloud_command expects args starting with 'gcloud'")

    gcloud = shutil.which("gcloud")
    if sys.platform == "win32" and gcloud and gcloud.lower().endswith((".cmd", ".bat")):
        return ["cmd", "/c", gcloud, *args[1:]]

    return [gcloud or "gcloud", *args[1:]]


def gcloud_run(args, *run_args, **run_kwargs):
    """Run gcloud with subprocess.run using the portable command wrapper."""
    return subprocess.run(gcloud_command(args), *run_args, **run_kwargs)
