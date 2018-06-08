from movements import path_clear, cleanup

def autonomous():
    try:
        path_clear()

    except KeyboardInterrupt:
        print("\nProgram Terminated")
        cleanup()

autonomous()
