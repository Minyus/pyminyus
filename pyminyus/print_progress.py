# -*- coding: utf-8 -*-

import sys
import time

def print_progress(iteration, total_iterations, update_interval_sec = 1.0):
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
        sys.stdout.write(f'\rProgress:{progress_pct: 5.2f} % ' \
                         + f' | Processed:{i_: d}/{total_iterations: d} ' \
                         + f' | Elapsed: {t_elapsed: 8.0f} sec' \
                         + f' | Est total: {t_est_total: 8.0f} sec' \
                         + f' | Est remained: {t_est_remained: 8.0f} sec' \
                        )
        sys.stdout.flush()
    if i == (total_iterations - 1):
        print()
        
### Example ###
if __name__ == "__main__":
    total_iterations = 100
    for i in range(total_iterations):
        print_progress(i, total_iterations)