from code_reader import Reader, create_mensa_file, repeat_function
from get_data import get_all
import os


if __name__ == '__main__':
    # repeats the function every minute
    repeat_function(create_mensa_file)
    
    reader = Reader(
        os.environ.get('PATH_ATTENDANCES'),
        # get_all()
        None
    )

    reader.start()