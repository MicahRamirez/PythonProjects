import cookie
import unittest

class TestCookie(unittest.TestCase):
    def setUp(self):
        self.cookie_state = cookie.ClickerState()

    def test_intial_state(self):
        initial_state = self.cookie_state.__str__()
        self.assertEqual(initial_state, ("Current-State: Total num cookies: 0."
        "0, Current num cookies: 0.0, Current Time: 0.0,"
        " Current Clicks per second: 1.0"))
       
        #test get_cookies on initial state
        self.assertEqual(self.cookie_state.get_cookies(), 0.0)
        #test get_cps on initial state
        self.assertEqual(self.cookie_state.get_cps(), 1.0)
        #test get_time on initial state
        self.assertEqual(self.cookie_state.get_time(), 0.0)
        #test time_until on initial state
        self.assertEqual(self.cookie_state.time_until(20), 20)

    def test_wait(self):
        self.cookie_state.wait(10)
        
        #test state after waiting 10 seconds
        self.assertEqual(self.cookie_state.get_cookies(), 10.0)
        #test time after waiting 10 seconds
        self.assertEqual(self.cookie_state.get_time(), 10.0)

    def test_time_until(self):
        self.cookie_state.wait(10)
        #test time_until 10 more cookies
        self.assertEqual(self.cookie_state.time_until(20), 10)

        #test time_until 10 cookies
        self.assertEqual(self.cookie_state.time_until(10), 0)

if __name__ == '__main__':
    unittest.main()
