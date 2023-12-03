def read_file(file_path):
    try:
        # Step 1: Open the file
        with open(file_path, 'r') as file:
            # Step 2: Read the file content
            lines = file.readlines()
            # Further processing or manipulation can be done here if needed
            return lines  # Return the list of strings
    except FileNotFoundError:
        print("File not found or unable to read the file.")
        return []  # Return an empty list if file not found or unable to read
    except Exception as e:
        print(f"An error occurred: {e}")
        return []  # Return an empty list for any other exception
    finally:
        # Step 3: Close the file (done automatically with 'with' statement)
        pass  # Nothing to do here as the 'with' statement handles file closure
