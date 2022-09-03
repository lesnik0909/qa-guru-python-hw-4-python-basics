def print_function_name_and_argument_value(call_function, *arguments):
    print("-----")
    print("Function name: " + call_function.__name__)
    if len(arguments) > 0:
        print("Arguments: ", *arguments)
    else:
        print("No arguments in function")


def open_browser(browser_name):
    print_function_name_and_argument_value(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_function_name_and_argument_value(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_function_name_and_argument_value(find_registration_button_on_login_page, page_url, button_text)


open_browser("Chrome")
go_to_companyname_homepage("Google")
find_registration_button_on_login_page("Google", "Python")
