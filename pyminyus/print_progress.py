""" my tool simpler than tqdm at https://github.com/Minyus/pyminyus/blob/master/pyminyus/print_progress.py
"""
import sys
import time
from datetime import datetime


def format_sec(s):
    m = s / 60
    h = m / 60
    d = h / 24
    if d >= 1:
        return "{:5.2f} days".format(d)
    if h >= 1:
        return "{:5.2f} hrs ".format(h)
    if m >= 1:
        return "{:5.2f} mins".format(m)
    return "{:5.2f} secs".format(s)


def timestamp():
    return datetime.now().strftime("%Y-%m-%dT%H%M%S")


class PrintProgress:
    def __init__(
        self, total_iterations, overwrite=False, update_interval_sec=1.0, prefix=""
    ):
        self.total_iterations = total_iterations
        self.last_iteration = total_iterations - 1
        self.overwrite = overwrite
        self.update_interval_sec = update_interval_sec
        t = time.time()
        self._time_started = self._time_updated = t
        self.prefix = prefix
        print("[{}] Initiated: {}".format(timestamp(), prefix))

    def print_progress(self, i):
        t = time.time()
        if ((t - self._time_updated) > self.update_interval_sec) or (
            i in [0, self.last_iteration]
        ):
            self._time_updated = t
            t_elapsed = t - self._time_started
            i_ = i + 1
            progress = i_ / self.total_iterations
            progress_pct = 100 * progress
            t_est_total = t_elapsed / progress
            t_est_remained = t_est_total - t_elapsed
            print_str = (
                "["
                + timestamp()
                + "] "
                + " | ".join(
                    [
                        self.prefix,
                        "{:d}/{:d}={:5.2f}%".format(
                            i_, self.total_iterations, progress_pct
                        ),
                        "Elapsed:{}".format(format_sec(t_elapsed)),
                        "Estimated:{}".format(format_sec(t_est_total)),
                        "Remained:{}".format(format_sec(t_est_remained)),
                        "",
                    ]
                )
            )

            if self.overwrite:
                # sys.stdout.write(print_str)
                # sys.stdout.flush()
                print(print_str, "\r", end="", flush=True)
            if not self.overwrite:
                print(print_str)
        if i == self.last_iteration:
            print()


if __name__ == "__main__":
    total_iterations = 10
    pp = PrintProgress(total_iterations=total_iterations)
    for i in range(total_iterations):
        time.sleep(1)
        pp.print_progress(i)
