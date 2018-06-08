import movements as mv

def auto():
    try:
        mv.path_clear()

    except KeyboardInterrupt:
        print("\nProgram Terminated")
        mv.cleanup()
