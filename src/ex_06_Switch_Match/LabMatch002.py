print("Enter which test you want to run")
test_type = input("Enter the test type: API,UI,Performance,Security")

match test_type:
    case "API":
        print("We are running a POSTMAN API.")
    case "UI":
        print("We are running a Selenium Test Case.")
    case "Performance":
        print("We are running a Selenium Performance Test Case.")
    case "Security":
        print("We are running a Selenium Security Test Case.")
    case _:
        print("Invalid Test Type.")

