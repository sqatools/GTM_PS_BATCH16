import pytest
import time
from Pages.Booking_page import BookingPage
@pytest.mark.usefixtures("get_driver_class") 
#due to this selenium knows that to run get_driver_class fixture before running the test cases in this class  
 


class TestBooking:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, get_driver_class):
        self.driver = get_driver_class
        self.BookingPageobj = BookingPage(self.driver)
        print("Test setup initiated")

    def test_booking_flow(self):
        # 1. Select an option on the booking page
        self.BookingPageobj.select_option()
        time.sleep(2)

        # 2. Enter booking details
        self.BookingPageobj.enter_booikng_details(
            first_name="Rushabh",
            last_name="Dhole",
            d_o_b="11/05/1995"
        )
        time.sleep(2)

        # 3. Select gender
        self.BookingPageobj.select_gender("male")        
        time.sleep(4)

        #4. Check title of the page
        actual_title = self.BookingPageobj.get_title()
        print("Actual Page name is ", actual_title)
