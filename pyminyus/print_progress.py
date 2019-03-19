import sys
import time

class PrintProgress():
    def __init__(self, total_iterations, overwrite=False, update_interval_sec=1.0):
        self.total_iterations = total_iterations
        self.last_iteration = total_iterations - 1
        self.overwrite = overwrite
        self.update_interval_sec = update_interval_sec
        t = time.time()
        self._time_started = self._time_updated = t

    def print_progress(self, i_):
        t = time.time()
        if ((t - self._time_updated) > self.update_interval_sec) or (i == self.last_iteration):
            self._time_updated = t
            t_elapsed = t - self._time_started
            progress = i_ / self.total_iterations
            progress_pct = 100 * progress
            t_est_total = t_elapsed / progress
            t_est_remained = t_est_total - t_elapsed
            print_str = \
                ( ' | Completed :{:d}/{:d} = {:5.2f} %'.format(i_, total_iterations, progress_pct) \
                + ' | Elapsed: {:6.0f} sec'.format(t_elapsed) \
                + ' | Est total: {:6.0f} sec'.format(t_est_total) \
                + ' | Est remained: {:6.0f} sec |'.format(t_est_remained) \
                )
            if self.overwrite:
                sys.stdout.write(print_str)
                sys.stdout.flush()
            if not self.overwrite:
                print(print_str)
        if (i == self.last_iteration): print()

if __name__ == "__main__":
    total_iterations = 20
    pp = PrintProgress(total_iterations = total_iterations)   
    for i in range(total_iterations):
        pp.print_progress(i)
        time.sleep(1)