import re # for regex expressions
import logging # for creating log files
import argparse # CLI arg parsing tool


def scanner(choice):


      # five files to choose from
      file_one = "Google_Maps_API_Key.txt"
      file_two = "Secret_Key.txt"
      file_three = "AWS_Account_ID.txt"
      file_four = "AWS_Access_ID_Key.txt"
      file_five = "Stripe_API_Key.txt"


      # five patterns to compare against the five files' contents
      pattern_one = r'AIza[0-9A-Za-z-_]{35}' # Google Maps API Key
      pattern_two = r"[0-9a-zA-Z/+]{40}" # AWS Secret Key
      pattern_three = r'^[0-9A-Z]{12}$' # AWS Account ID
      pattern_four = r'(AKIA)[0-9A-Z]{16}$' # AWS Access ID Key
      pattern_five = r'(sk_live_)[0-9a-zA-Z]{24}$' # Stripe API Key


      # argparse accepts an integer as its one argument
      # these conditionals assign each file to an integer
      # input type must be integer, directs scanner(choice) on which file to select to open
      if choice == 1:
            choice = file_one
      elif choice == 2:
            choice = file_two
      elif choice == 3:
            choice = file_three
      elif choice == 4:
            choice = file_four
      elif choice == 5:
            choice = file_five


      # read chosen file line by line
      with open(choice, "r") as f:
            for line_num, line in enumerate(f, start=1): # start at one to parse each line, rather than just read the contents in its entirety


            # search for regex matches
                  match_one = re.search(pattern_one, line)
                  match_two = re.search(pattern_two, line)
                  match_three = re.search(pattern_three, line)
                  match_four = re.search(pattern_four, line)
                  match_five = re.search(pattern_five, line)


        # conditionals for when a regex match is found
        # do not print lines that do not match the regex pattern
        # print the file name, line number, & matching string
                  if match_one:
                        print("File Name -> ", file_one, '\n'f"Line {line_num} -> {line.strip()}")
                  elif match_two:
                        print("File Name -> ", file_two, '\n'f"Line {line_num} -> {line.strip()}")
                  elif match_three:
                        print("File Name -> ", file_three, '\n'f"Line {line_num} -> {line.strip()}")
                  elif match_four:
                        print("File Name -> ", file_four, '\n'f"Line {line_num} -> {line.strip()}")
                  elif match_five:
                        print("File Name -> ", file_five, '\n'f"Line {line_num} -> {line.strip()}")


# argparse function
def main():
    

    # required syntax to set up argparse
    parser = argparse.ArgumentParser(description="This script creats a warning log if the file contents are accessed.")
    

    # user can get help if '-h' is passed as alongside the 'choice' argument
    parser.add_argument("choice", type=int, help="Enter 1, 2, 3, 4, or 5 to access files.")

    # capability to enable the verbose setting 
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

    args = parser.parse_args()

    if args.verbose:
          print("Verbose setting is enabled.")
    
    else:
      scanner(args.choice)
      logging.basicConfig(filename="Access Breached.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
      logger = logging.getLogger()
      logger.setLevel(logging.WARNING)
      logger.warning("WARNING - FILES LIST HAS BEEN ACCESSED") # warning log is only created if the scanner() function is called


if __name__ == "__main__":

    main()
