from splitters import IntegerProcessor
def main():
    # Instantiate math pipeline with your exact file
    processor = IntegerProcessor("integers.txt")
    # Run text splitting operations by calling its method
    processor.process_integers()
if __name__ == "__main__":
    main()