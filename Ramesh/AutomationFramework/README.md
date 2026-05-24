# Automation Framework

A comprehensive hybrid automation testing framework supporting both **UI (Selenium)** and **API (REST)** testing using **Pytest**.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Running Tests](#running-tests)
- [Test Configuration](#test-configuration)
- [Key Components](#key-components)
- [Test Flow](#test-flow)

---

## 🎯 Project Overview

This is a layered, modular automation framework that follows best practices:
- **Page Object Model (POM)** for UI testing
- **Separation of Concerns** with base classes, page objects, and tests
- **Centralized Test Data** management
- **Comprehensive Logging** and reporting
- **Pytest Markers** for test categorization (smoke, sanity, regression, f1)

---

## 🏗️ Architecture

### Layered Architecture

```
┌─────────────────────────────────────────┐
│     Test Layer (test_*.py)              │  <- Test Cases
├─────────────────────────────────────────┤
│  Page Objects / API Pages               │  <- Business Logic
│  (DummyPage, RestFullAPI)               │
├─────────────────────────────────────────┤
│  Base Classes                           │  <- Reusable Methods
│  (SeleniumBase, BaseAPI)                │
├─────────────────────────────────────────┤
│  Selenium / Requests Library            │  <- Driver & HTTP Client
└─────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
AutomationFramework/
├── api_data/                          # API configuration & session data
│   └── api_session_data.py            # URLs, headers, auth tokens
├── api_pages/                         # API abstraction layer
│   └── restfull_api_pages.py          # API operations (GET, POST, etc.)
├── base/                              # Base classes with reusable methods
│   ├── base_api.py                    # BaseAPI - HTTP methods wrapper
│   └── selenium_base.py               # SeleniumBase - Selenium wrapper
├── page_objects/                      # Page Object Model
│   └── dummy_page/
│       ├── dummy_page_class.py        # DummyPage - UI interactions
│       ├── dummy_page_locator.py      # DummyLocators - Element selectors
│       └── user_data.json             # Test data (cities, passengers, etc.)
├── test/                              # Test cases
│   ├── conftest.py                    # Pytest fixtures & setup
│   ├── api_test/
│   │   └── test_restfull_api.py       # API test cases
│   └── dummywebsite/
│       └── test_dummy_website_case.py # UI test cases
├── utilities/                         # Helper utilities
│   └── utils.py                       # JSON reader, common utilities
├── logs/                              # Test execution logs
│   ├── report.html                    # HTML report
│   └── assets/
│       └── style.css                  # Report styling
├── docs/                              # Documentation
├── pytest.ini                         # Pytest configuration
└── __init__.py

```

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Chrome browser (for UI tests)
- ChromeDriver (compatible with your Chrome version)

### Installation Steps

1. **Clone/Open the project**
```bash
cd AutomationFramework
```

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pytest selenium requests
```

---

## ▶️ Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test File
```bash
# UI tests only
pytest test/dummywebsite/test_dummy_website_case.py

# API tests only
pytest test/api_test/test_restfull_api.py
```

### Run Tests by Marker
```bash
# Smoke tests
pytest -m smoke

# Sanity tests
pytest -m sanity

# Regression tests
pytest -m regression

# F1 feature tests
pytest -m f1
```

### Run with Verbose Output
```bash
pytest -v
```

### Run with Logging
```bash
pytest -v --log-cli-level=INFO
```

### Generate HTML Report
```bash
pytest --html=logs/report.html --self-contained-html
```

---

## ⚙️ Test Configuration

### pytest.ini Configuration

```ini
[pytest]
markers =
    smoke: marker for smoke test cases
    sanity: marker for sanity test cases
    regression: marker for regression test cases
    f1: this is f1 feature marker

log_cli = True
log_cli_level = INFO
log_file = logs/executions.log
```

### conftest.py Fixture

The `get_driver_class` fixture handles browser initialization:
- Launches Chrome in **headless mode**
- Navigates to: `https://sqatools.in/dummy-booking-website/`
- Sets implicit wait: **10 seconds**
- Sets WebDriverWait timeout: **15 seconds**

---

## 🔧 Key Components

### 1. Base Layer (`/base/`)

#### SeleniumBase - Selenium Wrapper
Provides reusable methods for UI interactions:

```python
# Element Interactions
get_element(locator)                    # Find element with explicit wait
click_element(locator)                  # Click element
enter_text(locator, value)              # Enter text in field
get_element_text(locator)               # Get element text

# Verifications
check_element_is_displayed(locator)     # Verify element visibility
check_element_is_enabled(locator)       # Verify element is enabled
check_element_is_selected(locator)      # Verify element selection

# Dropdowns
select_dropdown_value(locator, value)   # Select dropdown by visible text

# Navigation
get_current_url()                       # Get current page URL
get_website_title()                     # Get page title
refresh_page()                          # Refresh the page
move_forward()                          # Browser forward
move_backword()                         # Browser back
```

#### BaseAPI - REST API Wrapper
Provides HTTP methods with logging:

```python
get_method(url, header, request_body)      # GET request
post_method(url, header, request_body)     # POST request
put_method(url, header, request_body)      # PUT request
patch_method(url, header, request_body)    # PATCH request
delete_method(url, header, request_body)   # DELETE request
```

### 2. Page Objects (`/page_objects/`)

#### DummyPage - UI Operations
Encapsulates booking website interactions:

```python
enter_source_and_destination(fromcity, destcity)  # Enter travel cities
select_gender(gender)                              # Select Male/Female
select_number_of_passengers(value)                 # Select passenger count
select_country(country_name)                       # Select country
```

#### DummyLocators - Element Selectors
Centralized locator definitions using Selenium's `By`:

```python
fromCityField = (By.ID, "fromcity")
DestCityField = (By.ID, "destcity")
male_radio_btn = (By.ID, "male")
female_radio_btn = (By.ID, "female")
passenger_dropdown = (By.ID, "admorepass")
contry_dropdown = (By.ID, "billing_country")
```

### 3. API Pages (`/api_pages/`)

#### RestFullAPI - API Operations
High-level API operations:

```python
get_all_objects()                    # Fetch all objects from restful-api.dev
get_one_object_details(object_id)    # Get specific object by ID
get_All_users()                      # Fetch users from GoRest API
```

### 4. Test Data (`/page_objects/dummy_page/user_data.json`)

```json
{
    "url": "https://sqatools.in/dummy-booking-website/",
    "fromCity": "Delhi",
    "destcity": "Guwahati",
    "no_of_passanger": "Add 2 more passenger (200%)",
    "gender_name": "female",
    "country_name": "India"
}
```

### 5. Utilities (`/utilities/`)

```python
read_json_data(filename)   # Read and parse JSON test data files
```

---

## 🔄 Test Flow

### UI Test Flow

```
1. conftest.py fixture (get_driver_class)
   ├── Launch Chrome in headless mode
   ├── Navigate to https://sqatools.in/dummy-booking-website/
   └── Maximize window & set implicit wait (10s)
   
2. Test Setup (setup fixture in test class)
   ├── Create DummyPage instance (inherits SeleniumBase)
   └── Load user_data.json using Utils.read_json_data()
   
3. Test Execution
   ├── Call DummyPage methods
   │   └── enter_source_and_destination(fromCity, destcity)
   ├── DummyPage calls SeleniumBase methods
   │   └── enter_text(locator, value)
   ├── SeleniumBase uses WebDriverWait to find element
   │   └── send_keys() to enter text
   └── Verify results
   
4. Cleanup
   └── Driver teardown (implicit in fixture yield)
```

### API Test Flow

```
1. Test Setup (setup fixture in test class)
   └── Create RestFullAPI instance (inherits BaseAPI)
   
2. Test Execution
   ├── Call RestFullAPI methods
   │   └── get_all_objects()
   ├── RestFullAPI calls BaseAPI methods
   │   └── get_method(url)
   ├── BaseAPI uses requests library
   │   └── requests.get(url, headers, data)
   └── Assert response
       ├── status_code == 200
       └── len(response.json()) == expected_count
```

---

## 📊 Test Examples

### UI Test Example

```python
@pytest.mark.usefixtures("get_driver_class")
class TestDummyWebsite:
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.dp = DummyPage(self.driver)
        self.util = Utils()
        self.user_data = self.util.read_json_data("page_objects/dummy_page/user_data.json")
    
    def test_enter_source_dest_city(self, request):
        """Test entering source and destination cities"""
        self.dp.enter_source_and_destination(
            self.user_data["fromCity"], 
            self.user_data["destcity"]
        )
    
    def test_select_gender(self):
        """Test selecting passenger gender"""
        self.dp.select_gender(gender=self.user_data["gender_name"])
```

### API Test Example

```python
class TestRestFullAPI():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.obj = RestFullAPI()
    
    def test_get_all_objects_and_verify(self):
        """Test retrieving all objects"""
        response = self.obj.get_all_objects()
        assert len(response.json()) == 13
        assert response.status_code == 200
```

---

## 📝 Logging

- **Console Logging**: INFO level logs displayed in console
- **File Logging**: All logs saved to `logs/executions.log`
- **Log Format**: `[timestamp] [level] (filename:lineno) message`

Example log output:
```
2024-05-22 10:15:30 [INFO] (selenium_base.py:18) getting element with locator : ('id', 'fromcity')
2024-05-22 10:15:31 [INFO] (selenium_base.py:24) entering text:Delhi in the locator : ('id', 'fromcity')
2024-05-22 10:15:32 [INFO] (base_api.py:12) Method Name : GET
```

---

## 🐛 Debugging

### Use PDB for Debugging
```python
import pdb; pdb.set_trace()
```

### Run Specific Test with Verbose Output
```bash
pytest -v -s test/dummywebsite/test_dummy_website_case.py::TestDummyWebsite::test_enter_source_dest_city
```

### Enable Detailed Logging
```bash
pytest -v --log-cli-level=DEBUG
```

---

## 📚 Best Practices

1. **Always use Page Object Model** - Keep test logic separated from page interaction logic
2. **Centralize Test Data** - Use JSON files for test data, not hardcoded values
3. **Use Descriptive Names** - Method and test names should clearly describe what they do
4. **Leverage Base Classes** - Reuse SeleniumBase and BaseAPI methods instead of writing custom code
5. **Wait Strategically** - Use explicit waits (WebDriverWait) for reliability
6. **Add Logging** - Use logger for debugging and reporting
7. **Clean Locators** - Keep locators in separate classes for maintainability

---

## 📦 Dependencies

- **pytest**: Test framework
- **selenium**: Web automation library
- **requests**: HTTP client for API testing

Install all dependencies:
```bash
pip install pytest selenium requests
```

---

## 🤝 Contributing

1. Follow the existing architecture and patterns
2. Add appropriate pytest markers for your tests
3. Update test data in JSON files, not in test code
4. Add logging statements for debugging
5. Keep methods in base classes generic and reusable

---

## 📄 License

This project is part of the automation training and development.

---

## 📞 Support

For issues or questions, refer to:
- `pytest.ini` - Test configuration
- `conftest.py` - Fixture setup
- `logs/executions.log` - Test execution logs

