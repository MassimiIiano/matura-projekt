from code_reader import Reader, create_mensa_file, repeat_function
import os


if __name__ == '__main__':
    # repeats the function every minute
    repeat_function(create_mensa_file)
    
    reader = Reader(
        os.environ.get('PATH_ATTENDANCES')
    )

    reader.start()