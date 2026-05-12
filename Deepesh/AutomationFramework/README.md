# Automation Framework

This is a Python-based test automation framework using **pytest** that supports both **API testing** and **Web UI testing** (using Selenium). It follows a modular, Page Object Model (POM) structure for maintainability and reusability.

## Key Components and Flow

### 1. **Base Layer** (`base/`)
- **`base_api.py`**: Contains `BaseAPI` class with HTTP methods (GET, POST, PUT, PATCH, DELETE) using the `requests` library. Each method logs request/response details.
- **`selenium_base.py`**: Contains `SeleniumBase` class that wraps Selenium WebDriver operations (click, enter text, select dropdowns, etc.) with explicit waits and logging.

### 2. **Page Objects Layer** (`page_objects/`)
- Implements Page Object Model for Web UI tests.
- Page classes (e.g., `DummyPage`) inherit from `SeleniumBase`.
- Separate locator classes (e.g., `DummyLocators`) define element locators using Selenium's `By` class.
- Example: `DummyPage` has methods like `enter_source_and_destination()`, `select_gender()`, etc., which use locators from `DummyLocators`.

### 3. **API Pages Layer** (`api_pages/`)
- API-specific classes (e.g., `RestFullAPI`) inherit from `BaseAPI`.
- Contain methods for API endpoints, using data from `api_data/`.
- Example: `RestFullAPI` has methods like `get_all_objects()`, `get_All_users()`.

### 4. **Data Layer** (`api_data/`, `page_objects/.../user_data.json`)
- **`api_session_data.py`**: Stores API URLs, headers, and authentication tokens.
- **`user_data.json`**: JSON file with test data for UI tests (e.g., form inputs).

### 5. **Test Layer** (`tests/`)
- **`conftest.py`**: Pytest fixtures for setup/teardown. Includes a `get_driver_class` fixture that launches a headless Chrome browser and navigates to the test site.
- Test classes use fixtures and instantiate page objects/API pages.
- Examples:
  - `TestRestFullAPI`: API tests calling methods from `RestFullAPI`.
  - `TestDummyWebsite`: UI tests using `DummyPage` and data from `user_data.json`.

### 6. **Utilities** (`utilities/`)
- **`utils.py`**: Helper class with methods like `read_json_data()` for loading test data from JSON files.

### 7. **Configuration** (`pytest.ini`)
- Defines pytest markers (smoke, sanity, regression, f1).
- Configures logging to console and file (`logs/executions.log`).
- Sets log levels and formats.

### 8. **Reports and Logs** (`logs/`, `docs/`)
- Test execution logs saved to `logs/executions.log`.
- HTML reports generated in `logs/report.html` with assets.

## Execution Flow
1. **Setup**: Pytest runs `conftest.py` fixtures to initialize drivers/sessions.
2. **Test Execution**:
   - For UI tests: Instantiate page objects → Call page methods → Interact with web elements via `SeleniumBase`.
   - For API tests: Instantiate API pages → Call API methods → Make HTTP requests via `BaseAPI`.
3. **Data Handling**: Test data loaded from JSON files using `Utils`.
4. **Logging**: All actions logged via Python's `logging` module.
5. **Teardown**: Fixtures handle cleanup (e.g., closing browser).

## Key Patterns
- **Inheritance**: Page/API classes extend base classes for shared functionality.
- **Separation of Concerns**: Locators, data, and logic are in separate files.
- **Fixtures**: Pytest fixtures manage test setup (e.g., browser launch).
- **Logging**: Comprehensive logging for debugging and reporting.

This framework is well-structured for scalable automation testing across web and API domains.