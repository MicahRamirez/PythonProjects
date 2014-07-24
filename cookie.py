"""
Cookie Clicker Simulator
"""
import time
import math

# Used to increase the timeout, if necessary


# Constants
#SIM_TIME = 10000000000.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_num_cookies = 0.0
        self._current_num_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0
        self._cookie_history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return ("Current-State: Total num cookies: " +str(self._total_num_cookies) + 
        ", Current num cookies: " + str(self._current_num_cookies) + ", Current Time: "
        + str(self._current_time) + ", Current Clicks per second: " +str(self. _current_cps))
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_num_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._cookie_history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        diff = cookies - self._current_num_cookies
        if diff == 0:
            return 0
        else:
            return int (diff/ self._current_cps)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        
        self._current_time += time
        cookies_in_time_elapsed = time * self._current_cps
        self._current_num_cookies += cookies_in_time_elapsed
        self._total_num_cookies += cookies_in_time_elapsed
         
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost > self._current_num_cookies:
            return None
        else:
            self._cookie_history.append((self._current_time, item_name,
                cost, self._total_num_cookies))
            self._current_cps += additional_cps
   
def simulate_clicker(build_info, duration, strategy):
    build_clone = build_info.clone()
    test = ClickerState()

    while test.get_time() < duration:
        item = strategy(test.get_cookies, test.get_cps(),
        duration - test.get_time(), build_info)

        if item == None:
            break
        else:
            #Find item cost
            cost = build_info.get_cost(item)
            time_to_wait = test.time_until(cost)
            test.wait(time_to_wait)
            test.buy_item(item, cost, build_info.get_cps(item))
            build_info.update_item(item)

def strategy_cheap(cookies, cps, time_left, build_info):
    money_available = time_left * cps
    too_poor = True
    list_items = build_info.build_items()
    list_items_cost = [for item in list_items build_info.get_cost(item)]
    cheapest = list_items.min()
        

