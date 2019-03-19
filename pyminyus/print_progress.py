import sys
import time


def print_progress(iteration, total_iterations, update_interval_sec = 1.0):
    """
    Show progress of loop iteration
    :param iteration: 0 for first iteration, 1 for next, and so on.
    :type iteration: int
    :param total_iterations: how many times the loop will iterate
    :type total_iterations: int
    :param update_interval_sec: how frequently the progress is updated
    :type update_interval_sec: float
    :return None
    :rtype None
    """
    global _time_started, _time_updated

    t = time.time()
    i = iteration
    if i==0:
        _time_started = _time_updated = t
    elif ((t - _time_updated) > update_interval_sec) or i == (total_iterations - 1) :
        _time_updated = t
        t_elapsed = t - _time_started
        i_ = i + 1
        progress = i_ / total_iterations
        progress_pct = 100 * progress
        t_est_total = t_elapsed / progress
        t_est_remained = t_est_total - t_elapsed
        sys.stdout.write('\rProgress:{:5.2f} % '.format(progress_pct) \
                         + ' | Completed :{:d}/{:d} '.format(i_, total_iterations) \
                         + ' | Elapsed: {:6.0f} sec'.format(t_elapsed) \
                         + ' | Est total: {:6.0f} sec'.format(t_est_total) \
                         + ' | Est remained: {:6.0f} sec'.format(t_est_remained) \
                        )
        sys.stdout.flush()
    if i == (total_iterations - 1):
        print()


if __name__ == "__main__":
    total_iterations = 100
    for i in range(total_iterations):
        print_progress(i, total_iterations)