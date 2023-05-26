import time
import pandas as pd

class FileReader:
    def run(self, file_path: str) -> pd.DataFrame:
        """
        Read a large CSV file in chunks and concatenate them into a single DataFrame

        Args:
            file_path (str): the path to the file to be read

        Returns:
            pd.DataFrame: the concatenated DataFrame
        """
        # Define the chunk size
        chunk_size = 10_000_000

        # Initialize an empty list to store the chunks
        chunks_list = []

        # Start the timer
        start_time = time.time()

        # Loop over the file by chunk
        chunks = pd.read_csv(file_path, chunksize=chunk_size, low_memory=False)
        for num, chunk in enumerate(chunks):
            print("reading chunk number ", num)
            chunks_list.append(chunk)

        # Concatenate the chunks into a single dataframe
        df = pd.concat(chunks_list, ignore_index=True)

        # End the timer
        end_time = time.time()

        # Calculate the elapsed time
        elapsed_time = end_time - start_time

        print(f"Time taken to read {file_path} using pandas: {elapsed_time:.2f} seconds")
        print(df.info)

        return df



if __name__ == "__main__":
    file_path = "data.csv"
    fr = FileReader()
    fr.run(file_path)