import pytest
import time
from Pages.bookingpage import BookingPage
@pytest.mark.usefixtures("get_driver_class") #due to this selenium knows that to run get_driver_class fixture before running the test cases in this class   
class TestBooking:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, get_driver_class):
        self.driver = get_driver_class
        self.booking_pageobj = BookingPage(self.driver)
        print("Test setup initiated")

    def test_booking_flow(self):
        # 1. Select an option on the booking page
        self.booking_pageobj.select_option()
        time.sleep(2)

        # 2. Enter booking details
        self.booking_pageobj.enter_booikng_details(
            first_name="Ekta",
            last_name="Gund",
            d_o_b="01/01/1990"
        )
        time.sleep(2)

        # 3. Select gender
        self.booking_pageobj.select_gender("female")        
        time.sleep(4)

        #4. Check title of the page
        actual_title = self.booking_pageobj.get_title()
        print("Actual Page name is ", actual_title)

   
