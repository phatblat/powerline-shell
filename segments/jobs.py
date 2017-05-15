import os
import re
import subprocess

# Fixed job count for Fish Shell
# https://github.com/banga/powerline-shell/issues/228
def add_jobs_segment():
    # pppid = subprocess.Popen(['ps', '-p', str(os.getppid()), '-o', 'ppid='], stdout=subprocess.PIPE).communicate()[0].strip()
    pppid = os.getppid()

    # -o ppid= removes the header row due to all headers being empty
    output = subprocess.Popen(['ps', '-a', '-o', 'ppid='], stdout=subprocess.PIPE).communicate()[0]

    # Why is this count 2 higher than expected?
    num_jobs = len(re.findall(str(pppid), output)) - 2

    if num_jobs > 0:
        powerline.append(' %d ' % num_jobs, Color.JOBS_FG, Color.JOBS_BG)

add_jobs_segment()
